import numpy as np
from scipy.stats import ttest_1samp

# Example data for hypothesis testing
data = np.array([28, 30, 25, 29, 27, 31, 26, 32, 30, 28])  # Sample data
null_mean = 30  # Null hypothesis mean

# One-sample t-test
t_stat, p_val = ttest_1samp(data, null_mean)

# Print test results
print("One-Sample t-Test:")
print("T-Statistic:", t_stat)
print("P-Value:", p_val)

# Interpretation based on p-value
alpha = 0.05  # Significance level
if p_val < alpha:
    print("Reject the null hypothesis. There is enough evidence to support the alternative hypothesis.")
else:
    print("Fail to reject the null hypothesis. There is not enough evidence to support the alternative hypothesis.")