import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Data
X = np.array([30, 40, 50, 60, 70, 80, 90, 100, 110, 120]).reshape(-1, 1)
y = np.array([10, 12, 15, 18, 20, 25, 28, 30, 35, 40])

# Model
model = LinearRegression()
model.fit(X, y)

# Coefficients
slope = model.coef_[0]
intercept = model.intercept_

print("Slope:", slope)
print("Intercept:", intercept)

# Prediction
new_income = np.array([85, 90, 26, 200, 10]).reshape(-1, 1)
predicted_spend = model.predict(new_income)

print("Predicted values:", predicted_spend)

# Plot
plt.scatter(X, y)
plt.plot(X, model.predict(X))
plt.scatter(new_income, predicted_spend)

plt.show()