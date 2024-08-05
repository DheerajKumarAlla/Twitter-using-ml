topics = []
for tweet in filtered_influencers['text']:
    blob = TextBlob(tweet)
    topics.append(blob.tags)
filtered_influencers['topics'] = topics

# Perform sentiment analysis
sentiments = []
for tweet in filtered_influencers['text']:
    blob = TextBlob(tweet)
    sentiments.append(blob.sentiment.polarity)
filtered_influencers['sentiment'] = sentiments

# Perform influence scoring
scaler = MinMaxScaler()
filtered_influencers['influence_score'] = 
scaler.fit_transform(filtered_influencers
[['follower_count', 'engagement_rate', 'sentiment']]).
mean(axis=1)

# Display the filtered influencers with the additional analysis
print(filtered_influencers)