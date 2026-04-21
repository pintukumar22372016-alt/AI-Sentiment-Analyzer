from sklearn.linear_model import LogisticRegression

# Training data
x = [[30], [40], [60], [80]]
y = [1, 1, 0, 1]

# Create and train model
model = LogisticRegression()
model.fit(x, y)

# Predict for 60
print(model.predict([[80]]))