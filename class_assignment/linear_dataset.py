import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# CSV load
df = pd.read_csv(r"C:\Users\pintu\OneDrive\Desktop\classpractice\class_assignment\Gold Price.csv")

# Columns check 
print(df.columns)
print(df.head())

# Date ko datetime me convert
df['Date'] = pd.to_datetime(df['Date'])

# Date ko numeric banaya (ML ke liye)
df['Date_num'] = df['Date'].map(pd.Timestamp.toordinal)

# Independent & dependent variable
X = df[['Date_num']]
y = df['Price']

# Model
model = LinearRegression()
model.fit(X, y)

# Prediction
y_pred = model.predict(X)

# GRAPH
plt.figure(figsize=(8,5))
plt.scatter(df['Date'], y, label="Actual Price")
plt.plot(df['Date'], y_pred, label="Predicted Line")
plt.xlabel("Date")
plt.ylabel("Gold Price")
plt.title("Gold Price Prediction Graph")
plt.legend()
plt.show()
