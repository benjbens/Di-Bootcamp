import pandas as pd
import numpy as np
import ssl


ssl._create_default_https_context = ssl._create_unverified_context


user = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user', delimiter='|')

# print(chipo)
# print(chipo.head(10))
# 4622 rows
#  5 columns
# print(list(chipo.columns))
# print(chipo[10:20:1].to_string())
# print(chipo.sort_values('quantity', ascending=False)[['item_name','quantity']].head(5).to_string())
# print(chipo['choice_description'].count())
# print(chipo['quantity'].sum())


# chipo['item_price'] = chipo['item_price'].apply(lambda s: s.strip('$')).astype(np.float32)
# num_str = '$2.39'
# strip_dollar = lambda s: s.strip('$')
# strip_dollar(num_str)
# print(chipo['item_price'].sum())
# print(chipo['quantity'].sum())
# print(chipo['quantity'].mean())
# print(chipo.loc[(chipo.item_price >= 10.00)].to_string())
# print(chipo.sort_values('item_price')['item_price', 'item_name'].to_string())
# print(chipo.sort_values('item_name')['item_name'].to_string())
# print(chipo.sort_values('item_price')['item_price'])
# print(chipo.loc[chipo.item_price == chipo.item_price.max()]['item_price'].count())
# print(chipo.loc[(chipo.item_name == 'Canned Soda') & (chipo.quantity > 1)].count())


# print(user[:].to_string())
print(list(user.columns))
# print(user.age.mean())
# print(user.loc[(user.gender == 'M')])
# print(user[['occupation', 'age']].groupby('occupation').max())
# print(user[['occupation', 'age']].groupby('occupation').max())
# print(user[['occupation', 'age']].groupby('occupation').mean())
print(user[['occupation', 'gender']].groupby('occupation'))
female = user['gender'] == 'F'
male = user['gender'] == 'M'
user['gender'] = male
user['gender'] = female
overall = user.shape[0]
mens_df = user.groupby(['occupation'])['gender'].sum()/overall

print(mens_df.to_string())
