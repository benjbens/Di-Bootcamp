import matplotlib.pyplot as plt
import numpy as np
import ssl
import pandas as pd
from dateutil.parser import parse
ssl._create_default_https_context = ssl._create_unverified_context


# Exercice 1

def myfun(start, step, length):
    stop = length * step + start + 1
    ask_user = np.arange(start, stop, step)
    print(ask_user)
    print(f"the stop is {stop}")

myfun(363, 71, 150)

# Exercice 2

x = np.array([1,2,3,np.nan,5,6,7,np.nan])
x = x[np.logical_not(np.isnan(x))]
print(x)


# Exercice 3

#
arr = np.random.randint(1, 100, (30,)).reshape(5, 6)
row_0 = arr[:,0]
row_1 = arr[:,1]
row_2 = arr[:,2]
row_3 = arr[:,3]
row_4 = arr[:,4]
print(row_0.max())
print(row_1.max())
print(row_2.max())
print(row_3.max())
print(row_4.max())


# EXercice 4

series = pd.Series(np.take(list('abcdefghijklmnop'), np.random.randint(16, size=500)))
print(series.value_counts().to_string())


# Exercice 5

series = pd.Series(['01 Jan 2020', '10-19-2020', '20150303', '2013/04/04', '2012-05-05', '2013-06-06T12:20'])
result = series.map(lambda iterator: parse(iterator))
print(series.to_string())
print(result)
print(result.dt.weekday)
print(result.dt.daysinmonth)
print(result.dt.dayofyear)


# Exercice 6

#
url = 'https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv'
df = pd.read_csv(url)
# df.dtypes.value_counts()
df.rename(columns={"Type": "TypeOfCar"}, inplace = True)
print(df)
naans = df.isna().sum()
print(naans, '\n')
print("Column with most nans:", naans.idxmax())


# Exercice 7
index_no = df.columns.get_loc('EngineSize')
index_no = df.columns.get_loc('Length')
print(index_no)
df = df.drop(df.columns[[11, 18]], axis=1)



df = df.drop(columns=['EngineSize', 'Length'])
print(list(df.columns))
print(set(['EngineSize', 'Length']).issubset(df.columns))

# Exercice 8

df1 = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
                    'weight': ['high', 'medium', 'low'] * 3,
                    'price': np.random.randint(0, 15, 9)})

df2 = pd.DataFrame({'pazham': ['apple', 'orange', 'pine'] * 2,
                    'kilo': ['high', 'low'] * 3,
                    'price': np.random.randint(0, 15, 6)})

frames = [df1, df2]
result = pd.concat(frames)
df = result.T.drop_duplicates().T
print(df)
naans = df.isna().sum()
print(naans)

# Exercice 9

df = pd.DataFrame(["STD,City\tState",
"33,Kolkata\tWest Bengal",
"44,Chennai\tTamil Nadu",
"40,Hyderabad\tTelengana",
"80,Bangalore\tKarnataka"], columns=['row'])



df = df.row.str.split(r',|\t', expand=True)
df = df.rename(columns=df.iloc[0]).drop(df.index[0])
print(df)



# Exercice 10



names = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model_year", "origin",
             "car_name"]
df_mpg = pd.read_csv("auto-mpg.data", header=None, names=names, delim_whitespace=True)

print(df_mpg.to_string())

def scatter_plot(df):
    plt.scatter(df.displacement, df.acceleration)
    plt.show()


scatter_plot(df_mpg)

# Exercice 11

def bar_plot(df):
    df = df[df.car_name.str.contains('toyota')]
    df = df[df["model_year"].isin([78])]
    plt.barplot(df['car_name'], df['cylinders'])

# Exercice 12

def line_plot(df):
    df=df[df.car_name.str.contains('toyota')]
    plt.plot(df.model_year, df.weight)
