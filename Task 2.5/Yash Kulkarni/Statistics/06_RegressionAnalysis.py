import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Generate random data for demonstration
np.random.seed(0)
X = 2 * np.random.rand(100, 1)  # Independent variable
y = 3 + 4 * X + np.random.randn(100, 1)  # Dependent variable with noise

# Add a constant term for the intercept (b0) in the multiple linear regression equation
X = sm.add_constant(X)

# Fit the regression model
model = sm.OLS(y, X).fit()

# Predictions
predictions = model.predict(X)

# Plot the data and regression line
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 1], y, label='Actual Data')
plt.plot(X[:, 1], predictions, color='red', label='Regression Line')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Simple Linear Regression')
plt.legend()
plt.grid(True)
plt.show()

# Summary of the regression model
print(model.summary())