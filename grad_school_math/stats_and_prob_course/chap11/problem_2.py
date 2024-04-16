import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Your data
data = {
    'Brand': ['Brand1', 'Brand1', 'Brand2', 'Brand2', 'Brand3', 'Brand3', 'Brand4', 'Brand4'],
    'Surface1': [709, 659, 668, 685, 659, 685, 698, 650],
    'Surface2': [713, 726, 722, 740, 666, 684, 704, 666],
    'Surface3': [660, 645, 692, 720, 678, 750, 686, 733]
}

# Convert the data to a pandas DataFrame
df = pd.DataFrame(data)

# Melt the DataFrame so it's in the right format for ANOVA
df_melted = df.melt(id_vars=['Brand'], var_name='Surface', value_name='Lifetime')

# Perform two-way ANOVA
model = ols('Lifetime ~ C(Brand) + C(Surface) + C(Brand):C(Surface)', data=df_melted).fit() # lifeetime (the value) approx equals these 3 effects
anova_results = sm.stats.anova_lm(model, typ=2)

print(anova_results)

