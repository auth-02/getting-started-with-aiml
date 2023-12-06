import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Generate sample data for a non-linear relationship
np.random.seed(0)
X = 2 * np.random.rand(100, 1) - 1
y = 2 * X**2 + 3 + np.random.randn(100, 1)  # Quadratic relationship with noise

# Add constant term for linear regression
X_with_const = sm.add_constant(X)

# Linear regression (assuming a linear relationship)
linear_model = sm.OLS(y, X_with_const).fit()

# Non-linear regression (quadratic model)
X_square = X ** 2
X_square_with_const = sm.add_constant(X_square)
non_linear_model = sm.OLS(y, X_square_with_const).fit()

# Visualize the data and both regression lines
plt.figure(figsize=(8, 6))
plt.scatter(X, y, label='Sample Data')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear vs. Non-Linear Regression')
plt.grid(True)

# Plot linear regression line
plt.plot(X, linear_model.predict(X_with_const), color='r', label='Linear Regression')

# Plot non-linear regression curve
x_vals = np.linspace(-1, 1, 100)
x_square_vals = x_vals ** 2
x_square_vals_with_const = sm.add_constant(x_square_vals)
plt.plot(x_vals, non_linear_model.predict(x_square_vals_with_const), color='g', label='Non-Linear Regression (Quadratic)')

plt.legend()
plt.show()
