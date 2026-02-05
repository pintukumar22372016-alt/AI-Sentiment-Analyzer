import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression

# CSV load
df = pd.read_csv(r"C:\Users\pintu\OneDrive\Desktop\classpractice\class_assignment\cleaned.csv")

print(df.columns)
print(df.head())

# Encode categorical column
le = LabelEncoder()
df['Type_of_collision_encoded'] = le.fit_transform(df['Type_of_collision'])

# Independent & dependent variable
X = df[['Type_of_collision_encoded']]
y = df['Accident_severity']

# Model
model = LinearRegression()
model.fit(X, y)

# Prediction
y_pred = model.predict(X)

# -------- GRAPH --------
plt.figure(figsize=(8,5))
plt.scatter(df['Type_of_collision_encoded'], y, label="Actual Severity")
plt.plot(df['Type_of_collision_encoded'], y_pred, color='red', label="Predicted Line")
plt.xlabel("Type of Collision (Encoded)")
plt.ylabel("Accident Severity")
plt.title("Accident Severity vs Type of Collision")
plt.legend()
plt.show()
