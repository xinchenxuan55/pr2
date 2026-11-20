import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression


data = pd.read_csv("training_data.csv")
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "linear_model.pkl")

with open("linear_model.txt", "w", encoding="utf-8") as file:
    file.write(f"Coefficients: {model.coef_}\n")
    file.write(f"Intercept: {model.intercept_}\n")

print("Model trained successfully.")
print(f"Coefficient: {model.coef_[0]:.6f}")
print(f"Intercept: {model.intercept_:.6f}")
