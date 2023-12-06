import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from scipy.stats import f_oneway

# Sample data for one-way ANOVA
group1 = np.random.normal(loc=10, scale=2, size=50)  # Group 1
group2 = np.random.normal(loc=12, scale=2, size=50)  # Group 2
group3 = np.random.normal(loc=15, scale=2, size=50)  # Group 3

# One-way ANOVA using SciPy
f_statistic, p_value = f_oneway(group1, group2, group3)

# Two-way ANOVA using Statsmodels
data = pd.DataFrame({'Group': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
                     'Variable': np.concatenate([group1, group2, group3])})
model = ols('Variable ~ C(Group)', data=data).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

# Print ANOVA results
print("One-Way ANOVA:")
print("F-Statistic:", f_statistic)
print("P-Value:", p_value)

print("\nTwo-Way ANOVA:")
print(anova_table)
