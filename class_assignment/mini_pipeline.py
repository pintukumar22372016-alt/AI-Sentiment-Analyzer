from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd

# Data
data = {
    'Temp': [30, 40, 50, 60],
    'Vibration': [2, 3, 4, 5],
    'Failure': [0, 0, 1, 1]
}

df = pd.DataFrame(data)

X = df[['Temp', 'Vibration']]
y = df['Failure']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

# Train
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
print(model.predict(X_test))
