import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis, norm

# Generate a sample dataset (normal distribution with added skewness and kurtosis)
data = np.random.normal(loc=0, scale=2, size=1000)
data = np.concatenate((data, np.random.normal(loc=8, scale=3, size=200)))  # Positive skewness and kurtosis

# Calculate skewness and kurtosis
skewness = skew(data)
kurt = kurtosis(data)

# Plot the histogram
plt.figure(figsize=(8, 6))
plt.hist(data, bins=30, density=True, alpha=0.6, color='g', label='Sample Data')
plt.title('Skewness and Kurtosis')
plt.xlabel('X')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)
plt.show()

print("Skewness:", skewness)
print("Kurtosis:", kurt)
