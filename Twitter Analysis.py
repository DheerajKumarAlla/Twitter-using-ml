from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Split the dataset into features (X) and target variable (y)
X = filtered_influencers[['follower_count', 'engagement_rate', 'sentiment']]
y = filtered_influencers['influence_score']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression model
model = LinearRegression()

# Train the model on the training data
model.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Rank the influencers based on the predicted influence scores
filtered_influencers['predicted_score'] = model.predict(X)
top_influencers = filtered_influencers.nlargest(3, 'predicted_score')

# Display the top influe