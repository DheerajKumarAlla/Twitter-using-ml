import tweepy
import pandas as pd

# Set up your Twitter API credentials
consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"
access_token = "your_access_token"
access_token_secret = "your_access_token_secret"

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create an API object
api = tweepy.API(auth)

# Search for influencers talking about statement 
# of purpose or academic writing
query = "statement of purpose OR academic writing"
influencers = []

# Iterate through search results
for tweet in tweepy.Cursor(api.search, q=query, 
tweet_mode='extended').items(100):
    if hasattr(tweet, 'retweeted_status'):
        text = tweet.retweeted_status.full_text
    else:
        text = tweet.full_text
    influencers.append({
        'username': tweet.user.screen_name,
        'text': text,
        'tweet_id': tweet.id,
        'created_at': tweet.created_at,
        'retweet_count': tweet.retweet_count,
        'favorite_count': tweet.favorite_count
    })

# Create a DataFrame from the influencer data
influencer_df = pd.DataFrame(influencers)

# Calculate the follower count and engagement rate
influencer_df['follower_count'] = 
influencer_df['username'].apply(lambda username: api.get_user(username).followers_count)
influencer_df['engagement_rate'] = 
(influencer_df['retweet_count'] + influencer_df['favorite_count']) / influencer_df['follower_count']


# Filter influencers based on reach, 
# engagement rate, and topic relevance
min_follower_count = 10000
min_engagement_rate = 0.03
relevant_keywords = ['statement of purpose', 
'academic writing', 'university admission']

filtered_influencers = influencer_df[
    (influencer_df['follower_count'] >= min_follower_count) &
    (influencer_df['engagement_rate'] >= min_engagement_rate) &
    (influencer_df['text'].str.contains
    ('|'.join(relevant_keywords), case=False))
]


# Display the filtered influencers
print(filtered_influencers)