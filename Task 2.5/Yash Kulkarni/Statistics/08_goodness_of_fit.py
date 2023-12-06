import numpy as np
from scipy.stats import chisquare

# Observed and expected frequencies (categorical data)
observed_freq = np.array([35, 45, 20])  # Example observed frequencies
expected_freq = np.array([30, 50, 20])  # Example expected frequencies from a model

# Chi-square goodness of fit test
chi2_stat, p_val = chisquare(f_obs=observed_freq, f_exp=expected_freq)

# Print test statistics and p-value
print("Chi-square Statistic:", chi2_stat)
print("P-Value:", p_val)

# Interpretation based on p-value
alpha = 0.05
if p_val < alpha:
    print("The model does not fit well (reject the null hypothesis).")
else:
    print("The model fits well (fail to reject the null hypothesis).")