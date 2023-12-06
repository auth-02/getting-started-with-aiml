import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, binom, poisson, uniform

# Normal Distribution
mean = 0
std_dev = 1
normal_data = np.random.normal(mean, std_dev, 1000)

# Binomial Distribution
n = 10
p = 0.5
binomial_data = np.random.binomial(n, p, 1000)

# Poisson Distribution
lambda_param = 2
poisson_data = np.random.poisson(lambda_param, 1000)

# Uniform Distribution
low = 0
high = 10
uniform_data = np.random.uniform(low, high, 1000)

# Plotting the distributions
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.hist(normal_data, bins=30, density=True, alpha=0.6, color='g')
plt.title('Normal Distribution')

plt.subplot(2, 2, 2)
plt.hist(binomial_data, bins=30, density=True, alpha=0.6, color='b')
plt.title('Binomial Distribution')

plt.subplot(2, 2, 3)
plt.hist(poisson_data, bins=30, density=True, alpha=0.6, color='r')
plt.title('Poisson Distribution')

plt.subplot(2, 2, 4)
plt.hist(uniform_data, bins=30, density=True, alpha=0.6, color='y')
plt.title('Uniform Distribution')

plt.tight_layout()
plt.show()
