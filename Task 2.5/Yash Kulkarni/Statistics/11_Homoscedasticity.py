import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Generate sample data with heteroscedasticity
np.random.seed(0)
X = 2 * np.random.rand(100, 1)
y = 5 + 3 * X + np.random.normal(loc=0, scale=X, size=(100, 1))

# Add constant term for the intercept
X_with_const = sm.add_constant(X)

# Fit linear regression model
model = sm.OLS(y, X_with_const).fit()

# Get residuals and predicted values
residuals = model.resid
predicted_values = model.fittedvalues

# Visualize residuals vs. predicted values
plt.figure(figsize=(8, 6))
plt.scatter(predicted_values, residuals, color='b', alpha=0.6)
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.title('Residuals vs. Predicted Values (Checking Homoscedasticity)')
plt.axhline(y=0, color='r', linestyle='--', linewidth=1)
plt.grid(True)
plt.show()

# Perform formal tests for heteroscedasticity
from statsmodels.stats.diagnostic import het_breuschpagan
_, p_value, _, _ = het_breuschpagan(residuals, X_with_const)
print("Breusch-Pagan Test P-Value:", p_value)

# Interpretation
alpha = 0.05
if p_value < alpha:
    print("The data shows evidence of heteroscedasticity (reject the null hypothesis).")
else:
    print("The data does not show evidence of heteroscedasticity (fail to reject the null hypothesis).")
