"""
Yujin Wang
Class: CS 521 - 22FALL
Date: December 6th, 2022
Final Project: Minimum Variance Portfolio
Description of Problem :
This program will give client investment suggestion.
By analysis, the industrial market condition, it will show the optimal investment portfolio.
"""
import pandas as pd
import numpy as np
from Investment import Investment

df0 = pd.read_excel("data.xlsx")
df1 = df0.iloc[:437, 1:]
column_names = list(df1.columns)

# remove null values from my data
for row_i in df1.index:
    if not df1.loc[row_i, column_names].isnull().sum():
        continue
    print("Row {} has a null value, dropping from dataframe".format(row_i))
    df1.drop(df0.index[row_i], inplace=True)


df_data = Investment(df1)
df_industry = df_data.industry_name
print(df_data)
stock_mean = df_data.mean
print(f'The mean returns of those stocks is \n{stock_mean}')
percent = df_data.mvp()
print(f'Ration of very stock in portfolio is \n {percent}')
assert np.matmul(stock_mean, percent) == 0.01198421078927915  # Confirm the final result
print('"+" means buy in, "-" means sell out \n')
print("Expected return of this portfolio is:")
print("{0:.3%}".format(np.matmul(stock_mean, percent)))
