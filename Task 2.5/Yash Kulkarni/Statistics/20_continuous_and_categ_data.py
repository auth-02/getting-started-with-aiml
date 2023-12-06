import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind, chi2_contingency

# Sample DataFrame with continuous and categorical data
data = {
    'Age': [25, 30, 35, 28, 40, 45, 22, 33, 29, 38],
    'Income': [50000, 55000, 60000, 48000, 70000, 75000, 45000, 62000, 58000, 68000],
    'Gender': ['M', 'F', 'M', 'F', 'M', 'M', 'F', 'M', 'F', 'M']
}

df = pd.DataFrame(data)

# Summary statistics for continuous data
print("Summary Statistics for Age:")
print(df['Age'].describe())

# Frequency table for categorical data
print("\nFrequency Table for Gender:")
print(df['Gender'].value_counts())

# One-hot encoding for categorical variable 'Gender'
df_encoded = pd.get_dummies(df, columns=['Gender'], drop_first=True)

# t-Test comparing means of 'Age' based on 'Gender'
t_stat, p_val = ttest_ind(df[df['Gender'] == 'M']['Age'], df[df['Gender'] == 'F']['Age'])
print("\nT-Test for Age between Genders:")
print("T-Statistic:", t_stat)
print("P-Value:", p_val)

# Chi-Square test for independence between 'Gender' and 'Income' categories
chi2_stat, p_val_chi2, _, _ = chi2_contingency(pd.crosstab(df['Gender'], pd.cut(df['Income'], bins=3)))
print("\nChi-Square Test for Independence (Income vs. Gender):")
print("Chi-Square Statistic:", chi2_stat)
print("P-Value:", p_val_chi2)

# Scatter plot for Age vs. Income colored by Gender
plt.figure(figsize=(8, 6))
plt.scatter(df['Age'], df['Income'], c=df_encoded['Gender_M'], cmap='coolwarm', label='M')
plt.scatter(df['Age'], df['Income'], c=~df_encoded['Gender_M'], cmap='coolwarm', marker='x', label='F')
plt.xlabel('Age')
plt.ylabel('Income')
plt.legend()
plt.title('Scatter Plot: Age vs. Income (Colored by Gender)')
plt.show()
