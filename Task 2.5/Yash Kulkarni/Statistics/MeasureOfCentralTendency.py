import numpy as np

# Sample dataset
data = np.array([2, 3, 4, 4, 6, 6, 6, 7, 8, 9])

# Measure of Frequency
frequency_dict = {}
for num in data:
    frequency_dict[num] = frequency_dict.get(num, 0) + 1
print("Frequency:", frequency_dict)

# Central Tendency
mean_value = np.mean(data)
median_value = np.median(data)
mode_value = np.argmax(np.bincount(data))

print("Mean:", mean_value)
print("Median:", median_value)
print("Mode:", mode_value)
