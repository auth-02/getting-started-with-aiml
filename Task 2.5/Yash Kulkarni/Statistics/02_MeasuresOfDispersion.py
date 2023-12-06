import numpy as np

# Sample dataset
data = np.array([2, 3, 4, 4, 6, 6, 6, 7, 8, 9])

# Range
data_range = np.ptp(data)

# Variance and Standard Deviation
variance_value = np.var(data)
std_deviation_value = np.std(data)

# Quartiles and IQR
Q1 = np.percentile(data, 25)
Q3 = np.percentile(data, 75)
iqr = Q3 - Q1

print("Range:", data_range)
print("Variance:", variance_value)
print("Standard Deviation:", std_deviation_value)
print("Q1:", Q1)
print("Q3:", Q3)
print("Interquartile Range (IQR):", iqr)