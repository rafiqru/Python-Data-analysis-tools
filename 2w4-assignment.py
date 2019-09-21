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


# calculation of centre and spread
summary1=data1['lifeexpectancy'].describe()
print(summary1)
summary2=data1['urbanrate'].describe()
print(summary2)
## for ANOVA make explanatory-urbanrate into into four categorical
data1['c_urbanrate']=pandas.cut(data1.urbanrate,[0,40,70,100])
#drop nan and make sub set
sub1=data1.dropna(subset=['lifeexpectancy','urbanrate'])
sub2=sub1.copy()
print(len(sub2))

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
#
# Moderator-incomeoeroerson
data1['incomeperperson']=pandas.to_numeric(data1['incomeperperson'], errors='coerce')
summary3=data1['incomeperperson'].describe()
print(summary3)
# cut incomeperperson into two groups upto 10000 and more than 10000
data1['c_incomeperperson']=pandas.cut(data1.incomeperperson,[0,10000,110000])
gf3=data1.groupby('c_incomeperperson').size()
print(gf3)
gp3=data1.groupby('c_incomeperperson').size()*100/len(data1)
print(gp3)
#drop nan and make sub set
sub3=data1.dropna(subset=['lifeexpectancy','c_urbanrate', 'c_incomeperperson'])
sub4=sub3.copy()
print(len(sub4))

##convert  c_incomeperperson to category 0 and 1 as follows
sub4['c_incomeperperson']=sub4.c_incomeperperson.astype('category').cat.codes
gf4=sub4.groupby('c_incomeperperson').size()
print(gf4)

## make another two subgroups
sub41=sub4[(sub4['c_incomeperperson']==0)]
sub42=sub4[(sub4['c_incomeperperson']==1)]
print(len(sub41))
print(len(sub42))

## run two ANOVA for two groups
print ('association between life expectancy (y) and urban rate of population (x) for those income <= 10000')
model2 = smf.ols(formula='lifeexpectancy ~ C(c_urbanrate)', data=sub41)
results2 = model2.fit()
print (results2.summary())

print ('association between life expectancy (y) and urban rate of population (x) for those income > 10000')
model3 = smf.ols(formula='lifeexpectancy ~ C(c_urbanrate)', data=sub42).fit()
print (model3.summary())


print ('means for life expectancy (y) by urban rate of population (x) for those income <= 10000')
m3= sub41.groupby('c_urbanrate').mean()
print (m3)
print ('means for life expectancy (y) by urban rate of population (x) for those income >10000')
m4 = sub42.groupby('c_urbanrate').mean()
print (m4)


#
data1['alcconsumption']=pandas.to_numeric(data1['alcconsumption'], errors='coerce')
summary6=data1['alcconsumption'].describe()
print(summary6)
# cut incomeperperson into two groups upto 10000 and more than 10000
data1['c_alcconsumption']=pandas.cut(data1.alcconsumption,[0,10,24])
gf6=data1.groupby('c_alcconsumption').size()
print(gf6)
gp3=data1.groupby('c_alcconsumption').size()*100/len(data1)
print(gp3)
#drop nan and make sub set
sub6=data1.dropna(subset=['lifeexpectancy','c_urbanrate', 'c_alcconsumption'])
print(len(sub6))

##convert  c_incomeperperson to category 0 and 1 as follows
data1['c_alcconsumption']=data1.c_alcconsumption.astype('category').cat.codes
gf7=data1.groupby('c_alcconsumption').size()
print(gf7)
sub6['c_alcconsumption']=sub6.c_alcconsumption.astype('category').cat.codes
gf7=sub6.groupby('c_incomeperperson').size()
print(gf7)
## make another two subgroups
sub61=sub6[(sub6['c_alcconsumption']==0)]
sub62=sub6[(sub6['c_alcconsumption']==1)]
print(len(sub61))
print(len(sub62))


print ('means for life expectancy (y) by urban rate of population (x) for those income <= 10000')
m5= sub61.groupby('c_alcconsumption').mean()
print (m5)
print ('means for life expectancy (y) by urban rate of population (x) for those income >10000')
m6 = sub62.groupby('c_alcconsumption').mean()
print (m6)

# from tuket hsd test it is found that there are signifucant deffernt all the groups excep first [0 30]and second [30 50]
