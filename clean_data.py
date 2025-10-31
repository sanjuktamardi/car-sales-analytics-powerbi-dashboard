import pandas as pd

# **Data loading** :
df = pd.read_csv('cars.csv')
print(df.head())

# Handling missing values :
total_missing_val = df.isnull().sum().sum()
print("\nThe total missing value is : ", total_missing_val) 
missing_val = df.isnull().sum()
print("\nThe missing values in the columns are :\n", missing_val) 
df['engine_capacity'].fillna(df['engine_capacity'].mean(), inplace=True)
print('after cleaning the missing data : ', df.isnull().sum().sum(),"\n",df.isnull().sum())

# duplicated values :
duplicate_val = df.duplicated().sum()
print("\nTotal Duplicated values : ", duplicate_val) 

df.drop_duplicates(inplace=True)
print('\nAfter cleaning duplicated values : ', df.duplicated().sum())
