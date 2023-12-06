import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Sample data for two-way ANOVA
np.random.seed(0)
factors = ['A', 'B'] * 30  # Two categorical factors
values = np.random.normal(loc=10, scale=2, size=60)  # Continuous outcome variable

# Create a DataFrame
data = pd.DataFrame({'Factor1': factors, 'Factor2': factors, 'Values': values})

# Two-way ANOVA using Statsmodels
model = ols('Values ~ C(Factor1) * C(Factor2)', data=data).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

# Print ANOVA results
print("Two-Way ANOVA:")
print(anova_table)