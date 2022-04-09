# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 14:37:35 2022

@author: Mangesh Mali
"""

import pandas

# Reading CSV Files with Pandas:
df = pandas.read_csv('C:\\Users\\Mangesh Mali\\Desktop\\Data\\User_Data.csv')
print(df)

# Writing CSV Files with Pandas:
df.to_csv('C:\\Users\\Mangesh Mali\\Desktop\Data\\IIT-B5.csv')
    
# Reading Excel Files with Pandas
df1 = pandas.read_excel('C:\\Users\\Mangesh Mali\\Desktop\\Data\\User_Data (1).xlsx')

df1 = pandas.read_excel('User_Data (1).xlsx')
print(df1)

# Writing Excel Files with Pandas 
df1.to_excel('IIT-B2.xlsx')
df2 = pandas.DataFrame(df1)
print (df2)
