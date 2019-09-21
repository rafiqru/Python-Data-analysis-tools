# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 11:28:17 2019

@author: mrafiq
"""
#w3 assignment data=gapminder:correlation coefficient
# research question:whether life expectancy (y) and urban rate of population (x) are correlated
#respone- -life ecpectancy(y) and explanatory-urban rate of population(x)
#H0: life expectancy (y) and urban rate of population(x) are not related
#Ha:life expectancy (y) and urban rate of population(x) are related
#load the libries
import pandas
import numpy
import seaborn
import scipy
import matplotlib.pyplot as plt
# read data 'nesarc in python
data1=pandas.read_csv('data_gapminder.csv', low_memory=False)
print(len(data1))
#all columns upper case
#data1.columns=map(str.upper,data1.columns)
#data type
data1.dtypes
#set pandas to to show all columns
pandas.set_option('display.max_columns', None)
#set pandas to to show all rows
pandas.set_option('display.max_rows', None)
# response is lifeexpectancy and explanatory variablevariable is urbanrate
#worked" convert to numeric as python read data as object(string)
data1['lifeexpectancy']=pandas.to_numeric(data1['lifeexpectancy'], errors='coerce')
data1['urbanrate']=pandas.to_numeric(data1['urbanrate'], errors='coerce')
data1.dtypes
#drop nan and make sub set
sub1=data1.dropna(subset=['lifeexpectancy','urbanrate'])
sub2=sub1.copy()
print(len(sub2))
#scatter plot
scat1 = seaborn.regplot(x='urbanrate', y='lifeexpectancy', fit_reg=True, data=sub2)
plt.xlabel('Urban Rate')
plt.ylabel('life Expectancy')
plt.title('Scatterplot for the Association Between Urban Rate and life Expectancy')

#
print ('association between urbanrate and life Expectancy')
print (scipy.stats.pearsonr(sub2['urbanrate'], sub2['lifeexpectancy']))

# conclusion: it is observed that the correlatiion between life expectancy (y) and urban rate of population (x)  is positive and modeately strong (r=0.62)
# increase ( or decrease ) in urban rate of population (x) also increase ( or decrease ) in life expectancy (y) and  
# as the p-value is very small, the relationship is statistically significant


