import numpy as np
from scipy.stats import chi2_contingency

# Example data for Chi-Square test for independence
observed_data = np.array([[30, 10], [15, 25]])  # Contingency table

# Chi-Square test for independence
chi2_stat, p_val, dof, expected = chi2_contingency(observed_data)

# Print test results
print("Chi-Square Test for Independence:")
print("Chi-Square Statistic:", chi2_stat)
print("Degrees of Freedom:", dof)
print("P-Value:", p_val)
print("Expected Frequencies:")
print(expected)

# Example data for Chi-Square goodness of fit test
observed_counts = np.array([25, 30, 15])  # Observed frequencies in a single categorical variable
expected_counts = np.array([20, 35, 15])  # Expected frequencies for comparison

# Chi-Square goodness of fit test
chi2_stat_goodness, p_val_goodness = chisquare(observed_counts, f_exp=expected_counts)

# Print goodness of fit test results
print("\nChi-Square Goodness of Fit Test:")
print("Chi-Square Statistic (Goodness of Fit):", chi2_stat_goodness)
print("P-Value (Goodness of Fit):", p_val_goodness)
