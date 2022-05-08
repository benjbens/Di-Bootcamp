import pandas as pd
import numpy as np
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
#
# titanic_df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
#
# Fare = titanic_df['Fare']
# Fare.head()
# # print(Fare.describe())
#
# f_min = Fare.loc[Fare <= 25]
# f_50 = Fare.loc[(Fare > 25) & (Fare < 50)]
# f_100 = Fare.loc[(Fare > 50) & (Fare < 100)]
# f_200 = Fare.loc[(Fare > 100) & (Fare < 200)]
# f_300 = Fare.loc[(Fare > 200) & (Fare < 300)]
# f_400 = Fare.loc[(Fare > 300) & (Fare < 400)]
# f_max = Fare.loc[Fare >= 500]
#
#
# mappings_min = {idx: 1 for idx in list(f_min.index)}
# mappings_50 = {idx: 2 for idx in list(f_50.index)}
# mappings_100 = {idx: 3 for idx in list(f_100.index)}
# mappings_200 = {idx: 4 for idx in list(f_200.index)}
# mappings_300 = {idx: 5 for idx in list(f_300.index)}
# mappings_400 = {idx: 6 for idx in list(f_400.index)}
# mappings_max = {idx: 7 for idx in list(f_max.index)}
#
# total_Fare_map = mappings_min | mappings_50 | mappings_100 | mappings_200 | mappings_300 | mappings_400 | mappings_max
#
# # print(total_Fare_map)
#
# Fare_updated = titanic_df.index.map(total_Fare_map)
# titanic_df['Fare'] = Fare_updated
# # print(titanic_df.head(100))


url = pd.read_csv ('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

print(url.to_string())

url['weightbinned'] = pd.cut(url.Weight, bins=range(0, 41, 10), retbins=False,include_lowest=True)