import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Define parameters for the normal distribution
mu = 0
sigma = 1

# Generate random data following normal distribution
data = np.random.normal(mu, sigma, 1000)

# Calculate PDF values for the data points
x = np.linspace(-5, 5, 1000)
pdf_values = norm.pdf(x, mu, sigma)

# Plot the normal distribution
plt.figure(figsize=(8, 6))
plt.plot(x, pdf_values, label='Normal Distribution PDF')
plt.hist(data, bins=30, density=True, alpha=0.6, color='g', label='Sample Data')
plt.title('Gaussian Normal Distribution')
plt.xlabel('X')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)
plt.show()
