# Continuous Function Example: sin(x) for x in [0, 2π]
import numpy as np
import matplotlib.pyplot as plt

x_continuous = np.linspace(0, 2*np.pi, 1000)
y_continuous = np.sin(x_continuous)

plt.figure(figsize=(8, 6))
plt.plot(x_continuous, y_continuous, label='sin(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Continuous Function: sin(x) for x in [0, 2π]')
plt.legend()
plt.grid(True)
plt.show()

# Discrete Function Example: f(x) = {1, 2, 3, 4, 5} for x in [1, 5]
x_discrete = np.array([1, 2, 3, 4, 5])
y_discrete = np.array([1, 2, 3, 4, 5])

plt.figure(figsize=(8, 6))
plt.scatter(x_discrete, y_discrete, color='r', label='Discrete Points')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Discrete Function: f(x) = {1, 2, 3, 4, 5} for x in [1, 5]')
plt.xticks(np.arange(1, 6))
plt.yticks(np.arange(1, 6))
plt.grid(True)
plt.legend()
plt.show()
