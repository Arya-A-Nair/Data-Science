import pandas as pd
import statsmodels.api as sm
import scipy.stats as stats


df=pd.read_csv("corrected_data.csv")

df_anova=df[['make','price']]
df_anova['price'] = pd.to_numeric(df_anova['price'], errors='coerce')

grouped_anova=df_anova.groupby('make',as_index=False)

#we get to know the price difference is low as p value is greater than 0.05 and F_stats is lesser than 1
anova_results_1=stats.f_oneway(grouped_anova.get_group("honda")["price"],grouped_anova.get_group("subaru")["price"])
#F_onewayResult(statistic=0.19744030127462606, pvalue=0.6609478240622193)

#we get to know the price difference is high as p value is larger than 0.05 and F_stats is greater than 1
anova_results_2=stats.f_oneway(grouped_anova.get_group("honda")["price"],grouped_anova.get_group("jaguar")["price"])
#F_onewayResult(statistic=400.925870564337, pvalue=1.0586193512077862e-11)

#there is a coorelation between categorical variable and other variable if F_test give large F value and small p value

print(anova_results_1)