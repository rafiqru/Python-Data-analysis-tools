# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 11:28:17 2019

@author: mrafiq
"""
#w1 assignment data=gapminder:ANOVA
# research question:whether life expectancy (y) depends on urban rate of population (x) 
#respone- -life ecpectancy(y) and explanatory-urban rate of population(x)
#H0: life expectancy (y) does not depend urban rate of population(x)
#Ha:life expectancy (y) depends urban rate of population(x)
#load the libries
import pandas
import numpy
import statsmodels.formula.api as smf
import statsmodels.stats.multicomp as multi 
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
# calculation of centre and spread
summary1=sub2['lifeexpectancy'].describe()
print(summary1)
sub2['urbanrate'].mean()
summary2=sub2['urbanrate'].describe()
print(summary2)
## for ANOVA make explanatory-urbanrate into into four categorical
sub2['c_urbanrate']=pandas.cut(sub2.urbanrate,[0,30,50,70,100])
#frequency
gf2=sub2.groupby('c_urbanrate').size()
print(gf2)
gp2=sub2.groupby('c_urbanrate').size()*100/len(sub2)
print(gp2)
# using ols function for calculating the F-statistic and associated p value
model1 = smf.ols(formula='lifeexpectancy ~ C(c_urbanrate)', data=sub2)
results1 = model1.fit()
print (results1.summary())

# comment: From ANOVA:As the p-value almost 0 we reject H0 and conclude that life expectancy (y) depends urban rate of population(x)
# that is means life expectancy of four urban groups are not eual
# we have conduct mutiple comparison  test:post hoc paired comparisons-tukeyhsd
mct1 = multi.MultiComparison(sub2['lifeexpectancy'], sub2['c_urbanrate'])
rest1 = mct1.tukeyhsd()
print(rest1.summary())
# from tuket hsd test it is found that there are signifucant deffernt all the groups excep first [0 30]and second [30 50]
