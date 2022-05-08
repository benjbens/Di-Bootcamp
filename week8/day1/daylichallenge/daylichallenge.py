import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


titanic_df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
# print(titanic_df.to_string())


sns.catplot(x='Sex', y='Age', data=titanic_df, kind="box")
# plt.show()


sns.catplot(x="Sex", y="Survived", hue="Pclass", kind="bar", data=titanic_df)
plt.show()


