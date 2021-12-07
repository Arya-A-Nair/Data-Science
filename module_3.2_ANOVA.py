import pandas as pd
import statsmodels.api as sm
import scipy.stats as stats


df=pd.read_csv("corrected_data.csv")

df_anova=df[['make','price']]
df_anova['price'] = pd.to_numeric(df_anova['price'], errors='coerce')

grouped_anova=df_anova.groupby('make',as_index=False)

anova_results_1=stats.f_oneway(grouped_anova.get_group("honda")["price"],grouped_anova.get_group("subaru")["price"])
print('')
print(anova_results_1)