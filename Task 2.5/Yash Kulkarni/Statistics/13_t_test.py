import numpy as np
from scipy.stats import ttest_ind, ttest_rel

# Example data for independent samples t-test
group1_scores = np.array([85, 89, 92, 78, 93])
group2_scores = np.array([88, 90, 87, 84, 91])

# Independent samples t-test
t_stat, p_val = ttest_ind(group1_scores, group2_scores)

# Print t-test results
print("Independent Samples t-Test:")
print("T-Statistic:", t_stat)
print("P-Value:", p_val)

# Example data for paired samples t-test
before_scores = np.array([55, 60, 50, 58, 62])
after_scores = np.array([58, 62, 53, 61, 64])

# Paired samples t-test
t_stat_paired, p_val_paired = ttest_rel(before_scores, after_scores)

# Print paired samples t-test results
print("\nPaired Samples t-Test:")
print("T-Statistic (Paired):", t_stat_paired)
print("P-Value (Paired):", p_val_paired)
