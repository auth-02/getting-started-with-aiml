import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Sample data for one-way ANOVA
group1 = np.random.normal(loc=10, scale=2, size=50)  # Group 1
group2 = np.random.normal(loc=12, scale=2, size=50)  # Group 2
group3 = np.random.normal(loc=15, scale=2, size=50)  # Group 3

# One-way ANOVA using SciPy
f_statistic, p_value = f_oneway(group1, group2, group3)

# Print ANOVA results
print("One-Way ANOVA:")
print("F-Statistic:", f_statistic)
print("P-Value:", p_value)

# Perform post-hoc Tukey's HSD test
data = pd.DataFrame({'Values': np.concatenate([group1, group2, group3]),
                     'Groups': ['Group 1'] * 50 + ['Group 2'] * 50 + ['Group 3'] * 50})
tukey_results = pairwise_tukeyhsd(data['Values'], data['Groups'])

# Print Tukey's HSD test results
print("\nTukey's HSD Test:")
print(tukey_results)