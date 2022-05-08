import matplotlib.pyplot as plt
import numpy as np
import ssl
import pandas as pd
from dateutil.parser import parse
ssl._create_default_https_context = ssl._create_unverified_context




df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
pd.get_dummies(df, columns=['species'])

means = df[['Manufacturer', 'Make']].groupby('Manufacturer').mean()
df['Manufacturer_transformed'] = df['Manufacturer'].dropna().apply(lambda x: means.loc[x, "Make"])
df[['Manufacturer', 'Manufacturer_transformed', 'Make']].head()

print(df)
