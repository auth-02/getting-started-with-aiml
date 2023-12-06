import numpy as np
from scipy.stats import norm

# Example data for one-sample z-test
sample_mean = 75  # Sample mean
population_mean = 70  # Known population mean
population_stddev = 10  # Known population standard deviation
sample_size = 100  # Sample size

# One-sample z-test
z_score = (sample_mean - population_mean) / (population_stddev / np.sqrt(sample_size))
p_value_one_sample = 1 - norm.cdf(z_score)  # One-tailed test, assuming sample mean > population mean

# Print one-sample z-test results
print("One-Sample z-Test:")
print("Z-Score:", z_score)
print("P-Value:", p_value_one_sample)

# Example data for two-sample z-test
sample1_mean = 75  # Sample 1 mean
sample2_mean = 72  # Sample 2 mean
stddev1 = 8  # Population standard deviation of sample 1
stddev2 = 7  # Population standard deviation of sample 2
sample1_size = 150  # Sample 1 size
sample2_size = 120  # Sample 2 size

# Two-sample z-test
pooled_stddev = np.sqrt((stddev1**2 / sample1_size) + (stddev2**2 / sample2_size))
z_score_two_sample = (sample1_mean - sample2_mean) / pooled_stddev
p_value_two_sample = 1 - norm.cdf(z_score_two_sample)  # One-tailed test, assuming sample1_mean > sample2_mean

# Print two-sample z-test results
print("\nTwo-Sample z-Test:")
print("Z-Score (Two-Sample):", z_score_two_sample)
print("P-Value (Two-Sample):", p_value_two_sample)
