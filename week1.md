# Python-Data-analysis-tools
## week-1 assignment
## Data-analysis-tools: week 1 assignment
#w1 assignment data=gapminder:ANOVA
# research question:whether life expectancy (y) depends on urban rate of population (x)
#respone- -life ecpectancy(y) and explanatory-urban rate of population(x)
#H0: life expectancy (y) does not depend urban rate of population(x)
#Ha:life expectancy (y) depends urban rate of population(x)
Results:
runfile(‘E:/1 Python/2. Data-analysis-tools/2w1-assignment.py’, wdir='E:/1 Python/2. Data-analysis-tools’)
213
188
count    188.000000
mean      69.600702
std        9.708289
min       47.794000
25%       63.952250
50%       73.126500
75%       76.236750
max       83.394000
Name: lifeexpectancy, dtype: float64
count    188.000000
mean      55.932766
std       23.286464
min       10.400000
25%       36.745000
50%       57.230000
75%       73.465000
max      100.000000
Name: urbanrate, dtype: float64
c_urbanrate
(0, 30]      34
(30, 50]     42
(50, 70]     57
(70, 100]    55
dtype: int64
c_urbanrate
(0, 30]      18.085106
(30, 50]     22.340426
(50, 70]     30.319149
(70, 100]    29.255319
dtype: float64
                           OLS Regression Results                            
==============================================================================
Dep. Variable:         lifeexpectancy   R-squared:                       0.368
Model:                            OLS   Adj. R-squared:                  0.358
Method:                 Least Squares   F-statistic:                     35.72
Date:                Mon, 16 Sep 2019   Prob (F-statistic):           3.07e-18
Time:                        10:38:35   Log-Likelihood:                -650.44
No. Observations:                 188   AIC:                             1309.
Df Residuals:                     184   BIC:                             1322.
Df Model:                           3                                        
Covariance Type:            nonrobust                                        
=======================================================================================================================
                                                         coef    std err          t      P>|t|      [0.025      0.975]
———————————————————————————————————————–
Intercept                                              62.0020      1.334     46.466      0.000      59.369      64.635
C(c_urbanrate)[T.Interval(30, 50, closed='right’)]      1.7141      1.795      0.955      0.341      -1.827       5.255
C(c_urbanrate)[T.Interval(50, 70, closed='right’)]      9.5081      1.686      5.640      0.000       6.182      12.834
C(c_urbanrate)[T.Interval(70, 100, closed='right’)]    14.8110      1.697      8.726      0.000      11.462      18.160
==============================================================================
Omnibus:                       10.031   Durbin-Watson:                   1.861
Prob(Omnibus):                  0.007   Jarque-Bera (JB):               10.701
Skew:                          -0.583   Prob(JB):                      0.00475
Kurtosis:                       2.914   Cond. No.                         5.57
==============================================================================
Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
  Multiple Comparison of Means - Tukey HSD, FWER=0.05  
=========================================================
group1    group2  meandiff p-adj   lower   upper  reject
———————————————————
(0, 30]  (30, 50]   1.7141 0.7497 -2.9398  6.3681  False
(0, 30]  (50, 70]   9.5081  0.001  5.1367 13.8795   True
(0, 30] (70, 100]   14.811  0.001   10.41  19.212   True
(30, 50]  (50, 70]   7.7939  0.001  3.6916 11.8963   True
(30, 50] (70, 100]  13.0969  0.001   8.963 17.2307   True
(50, 70] (70, 100]   5.3029 0.0022  1.4899  9.1159   True
———————————————————
Conclusion:From ANOVA: As the p-value almost 0 we reject H0 and conclude that life expectancy (y) depends urban rate of population(x)
 that is means life expectancy of four urban groups are not equal.
# we have conduct multiple comparison  test:post hoc paired comparisons-tukeyhsd  test it is found that there are significant deffer all the groups except first [0 30]and second [30 50]

Python code:
Created on Mon Sep  9 11:28:17 2019
@author: mrafiq
“”“
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
data1=pandas.read_csv('data_gapminder.csv’, low_memory=False)
print(len(data1))
#all columns upper case
#data1.columns=map(str.upper,data1.columns)
#data type
data1.dtypes
#set pandas to to show all columns
pandas.set_option('display.max_columns’, None)
#set pandas to to show all rows
pandas.set_option('display.max_rows’, None)
# response is lifeexpectancy and explanatory variablevariable is urbanrate
#worked” convert to numeric as python read data as object(string)
data1['lifeexpectancy’]=pandas.to_numeric(data1['lifeexpectancy’], errors='coerce’)
data1['urbanrate’]=pandas.to_numeric(data1['urbanrate’], errors='coerce’)
data1.dtypes
#drop nan and make sub set
sub1=data1.dropna(subset=['lifeexpectancy’,'urbanrate’])
sub2=sub1.copy()
print(len(sub2))
# calculation of centre and spread
summary1=sub2['lifeexpectancy’].describe()
print(summary1)
sub2['urbanrate’].mean()
summary2=sub2['urbanrate’].describe()
print(summary2)
## for ANOVA make explanatory-urbanrate into into four categorical
sub2['c_urbanrate’]=pandas.cut(sub2.urbanrate,[0,30,50,70,100])
#frequency
gf2=sub2.groupby('c_urbanrate’).size()
print(gf2)
gp2=sub2.groupby('c_urbanrate’).size()*100/len(sub2)
print(gp2)
# using ols function for calculating the F-statistic and associated p value
model1 = smf.ols(formula='lifeexpectancy ~ C(c_urbanrate)’, data=sub2)
results1 = model1.fit()
print (results1.summary())

