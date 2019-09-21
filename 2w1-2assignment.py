# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 16:58:25 2019

@author: DELL PC
"""
#w2 assignment: chi square test
# research question: whether drinking alchole depend on marital status who have family history of drinking
#load the libries
import pandas
import numpy
import scipy.stats
import seaborn
import matplotlib.pyplot as plt
# read data 'nesarc in python
data1=pandas.read_csv('my_nesarc.csv', low_memory=False)
print(len(data1))
#all columns upper case
data1.columns=map(str.upper,data1.columns)

#data type
data1.dtypes

#worked" convert to numeric as python read data as object(string)
data1['S2DQ1']=pandas.to_numeric(data1['S2DQ1'], errors='coerce')
data1['S2AQ3']=pandas.to_numeric(data1['S2AQ3'], errors='coerce')
data1['MARITAL']=pandas.to_numeric(data1['MARITAL'], errors='coerce')
data1.dtypes
#replacing missing values for nan (ALSO 9 OR 99 CONSIDERING MISSING)
print('count for original S2DQ1')
f1=data1['S2DQ1'].value_counts(sort=False,dropna=False)
print(f1)
print('count for S2DQ1 by replacing missing with nan')
data1['S2DQ1']=data1['S2DQ1'].replace(9, numpy.nan)
f11=data1['S2DQ1'].value_counts(sort=False, dropna=False)
print(f11)
print('count for original S2AQ3')
f2=data1['S2AQ3'].value_counts(sort=False,dropna=False)
print(f2)
print('count for S2AQ3 by replacing missing with nan')
data1['S2AQ3']=data1['S2AQ3'].replace(9,numpy.nan)
f22=data1['S2AQ3'].value_counts(sort=False, dropna=False)
print(f22)
print('count for original MARITAL')
f3=data1['MARITAL'].value_counts(sort=False,dropna=False)
print(f3) # no missing values

# select rows: subset of data1 given that FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER’
sub1=data1[(data1['S2DQ1']==1)]
print(len(sub1))
# drop na values
#sub2=sub1.dropna()


#also drop nan and make another sub set
sub2=sub1[['MARITAL','S2AQ3']]
sub3=sub2.dropna()
print(len(sub3))

#frequency
f4=sub3['S2AQ3'].value_counts()
print(f4)
f5=sub3['MARITAL'].value_counts()
print(f5)
# contingency table of observed counts
cto=pandas.crosstab(sub3['S2AQ3'], sub3['MARITAL'], margins=True)
print (cto)

# column percentages
colsum=cto.sum(axis=0)
colpt=cto/colsum
print(colpt)

# chi-square
print ('chi-square value, p value, expected counts')
cs1= scipy.stats.chi2_contingency(cto)
print (cs1)

# Conclusion: as the p value is very small we can conclude that  drinking alchole depend on marital status who have family history of drinking
#(FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER)
# for chi square we do not need need to run post hoc paired comparisons test







