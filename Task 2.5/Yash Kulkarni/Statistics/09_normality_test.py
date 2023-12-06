import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Generate a sample dataset (normal distribution for demonstration)
np.random.seed(0)
data = np.random.normal(loc=0, scale=1, size=1000)

# Graphical methods for normality assessment
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.hist(data, bins=30, density=True, alpha=0.6, color='g')
plt.title('Histogram: Normality Assessment')

plt.subplot(1, 2, 2)
stats.probplot(data, dist="norm", plot=plt)
plt.title('Q-Q Plot: Normality Assessment')

plt.tight_layout()
plt.show()

# Statistical tests for normality
shapiro_test_stat, shapiro_p_value = stats.shapiro(data)
ks_test_stat, ks_p_value = stats.kstest(data, 'norm')

print("Shapiro-Wilk Test:")
print("Test Statistic:", shapiro_test_stat)
print("P-Value:", shapiro_p_value)
print("Kolmogorov-Smirnov Test:")
print("Test Statistic:", ks_test_stat)
print("P-Value:", ks_p_value)

# Interpretation based on p-values
alpha = 0.05
if shapiro_p_value > alpha and ks_p_value > alpha:
    print("The data appears to be normally distributed (fail to reject the null hypothesis).")
else:
    print("The data does not appear to be normally distributed (reject the null hypothesis).")
