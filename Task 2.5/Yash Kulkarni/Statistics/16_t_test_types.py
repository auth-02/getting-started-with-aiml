import numpy as np
from scipy.stats import ttest_ind, ttest_rel, ttest_1samp

# Example data for t-tests
group1_scores = np.array([85, 89, 92, 78, 93])  # Independent samples for independent t-test
group2_scores = np.array([88, 90, 87, 84, 91])
before_scores = np.array([55, 60, 50, 58, 62])  # Paired samples for paired t-test
after_scores = np.array([58, 62, 53, 61, 64])
sample_data = np.array([28, 30, 25, 29, 27, 31, 26, 32, 30, 28])  # Sample data for one-sample t-test
null_mean = 30  # Known population mean for one-sample t-test

# Independent samples t-test
t_stat_ind, p_val_ind = ttest_ind(group1_scores, group2_scores)
print("Independent Samples t-Test:")
print("T-Statistic:", t_stat_ind)
print("P-Value:", p_val_ind)

# Paired samples t-test
t_stat_paired, p_val_paired = ttest_rel(before_scores, after_scores)
print("\nPaired Samples t-Test:")
print("T-Statistic (Paired):", t_stat_paired)
print("P-Value (Paired):", p_val_paired)

# One-sample t-test
t_stat_one_sample, p_val_one_sample = ttest_1samp(sample_data, null_mean)
print("\nOne-Sample t-Test:")
print("T-Statistic (One-Sample):", t_stat_one_sample)
print("P-Value (One-Sample):", p_val_one_sample)