# Python-Data-analysis-tools

## W4 assignment data=ANOVA and ANOVA with moderator
runfile(‘E:/1 Python/2. Data-analysis-tools/2w4-finalassignment.py’, wdir='E:/1 Python/2. Data-analysis-tools’)
213
count    191.000000
mean      69.753524
std        9.708621
min       47.794000
25%       64.447000
50%       73.131000
75%       76.593000
max       83.394000
Name: lifeexpectancy, dtype: float64
count    203.000000
mean      56.769360
std       23.844933
min       10.400000
25%       36.830000
50%       57.940000
75%       74.210000
max      100.000000
Name: urbanrate, dtype: float64
188
c_urbanrate
(0, 40]      56
(40, 70]     77
(70, 100]    55
dtype: int64
c_urbanrate
(0, 40]      29.787234
(40, 70]     40.957447
(70, 100]    29.255319
dtype: float64
                           OLS Regression Results                            
==============================================================================
Dep. Variable:         lifeexpectancy   R-squared:                       0.373
Model:                            OLS   Adj. R-squared:                  0.366
Method:                 Least Squares   F-statistic:                     55.04
Date:                Wed, 18 Sep 2019   Prob (F-statistic):           1.76e-19
Time:                        16:25:41   Log-Likelihood:                -649.69
No. Observations:                 188   AIC:                             1305.
Df Residuals:                     185   BIC:                             1315.
Df Model:                           2                                        
Covariance Type:            nonrobust                                        
=======================================================================================================================
                                                         coef    std err          t      P>|t|      [0.025      0.975]
———————————————————————————————————————–
Intercept                                              61.5031      1.033     59.552      0.000      59.466      63.541
C(c_urbanrate)[T.Interval(40, 70, closed='right’)]      8.8351      1.357      6.509      0.000       6.157      11.513
C(c_urbanrate)[T.Interval(70, 100, closed='right’)]    15.3099      1.467     10.435      0.000      12.415      18.204
==============================================================================
Omnibus:                        9.502   Durbin-Watson:                   1.967
Prob(Omnibus):                  0.009   Jarque-Bera (JB):               10.136
Skew:                          -0.559   Prob(JB):                      0.00629
Kurtosis:                       2.789   Cond. No.                         3.95
==============================================================================
Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
 Multiple Comparison of Means - Tukey HSD, FWER=0.05  
========================================================
group1    group2  meandiff p-adj  lower   upper  reject
——————————————————–
(0, 40]  (40, 70]   8.8351 0.001  5.6279 12.0423   True
(0, 40] (70, 100]  15.3099 0.001 11.8431 18.7767   True
(40, 70] (70, 100]   6.4748 0.001  3.2507  9.6988   True
——————————————————–
count    187.000000
mean       6.689412
std        4.899617
min        0.030000
25%        2.625000
50%        5.920000
75%        9.925000
max       23.010000
Name: alcconsumption, dtype: float64
c_alcconsumption
(0, 10]     142
(10, 25]     45
dtype: int64
c_alcconsumption
(0, 10]     66.666667
(10, 25]    21.126761
dtype: float64
176
c_alcconsumption
0    134
1     42
dtype: int64
134
42
association between life expectancy (y) and urban rate of population (x) for those alcconsumptionn<=10
                           OLS Regression Results                            
==============================================================================
Dep. Variable:         lifeexpectancy   R-squared:                       0.362
Model:                            OLS   Adj. R-squared:                  0.352
Method:                 Least Squares   F-statistic:                     37.16
Date:                Wed, 18 Sep 2019   Prob (F-statistic):           1.65e-13
Time:                        16:25:41   Log-Likelihood:                -466.52
No. Observations:                 134   AIC:                             939.0
Df Residuals:                     131   BIC:                             947.7
Df Model:                           2                                        
Covariance Type:            nonrobust                                        
=======================================================================================================================
                                                         coef    std err          t      P>|t|      [0.025      0.975]
———————————————————————————————————————–
Intercept                                              60.7872      1.114     54.567      0.000      58.584      62.991
C(c_urbanrate)[T.Interval(40, 70, closed='right’)]      8.0042      1.583      5.056      0.000       4.872      11.136
C(c_urbanrate)[T.Interval(70, 100, closed='right’)]    15.1006      1.777      8.496      0.000      11.585      18.617
==============================================================================
Omnibus:                        7.574   Durbin-Watson:                   2.071
Prob(Omnibus):                  0.023   Jarque-Bera (JB):                5.550
Skew:                          -0.375   Prob(JB):                       0.0623
Kurtosis:                       2.342   Cond. No.                         3.58
==============================================================================
Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
association between life expectancy (y) and urban rate of population (x) for those alcconsumption > 10
                           OLS Regression Results                            
==============================================================================
Dep. Variable:         lifeexpectancy   R-squared:                       0.215
Model:                            OLS   Adj. R-squared:                  0.174
Method:                 Least Squares   F-statistic:                     5.330
Date:                Wed, 18 Sep 2019   Prob (F-statistic):            0.00899
Time:                        16:25:41   Log-Likelihood:                -139.30
No. Observations:                  42   AIC:                             284.6
Df Residuals:                      39   BIC:                             289.8
Df Model:                           2                                        
Covariance Type:            nonrobust                                        
=======================================================================================================================
                                                         coef    std err          t      P>|t|      [0.025      0.975]
———————————————————————————————————————–
Intercept                                              66.7945      3.461     19.299      0.000      59.794      73.795
C(c_urbanrate)[T.Interval(40, 70, closed='right’)]      6.2123      3.762      1.651      0.107      -1.398      13.823
C(c_urbanrate)[T.Interval(70, 100, closed='right’)]    11.4518      3.870      2.959      0.005       3.625      19.279
==============================================================================
Omnibus:                       18.384   Durbin-Watson:                   2.060
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               23.248
Skew:                          -1.445   Prob(JB):                     8.95e-06
Kurtosis:                       5.221   Cond. No.                         6.89
==============================================================================
Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
means for life expectancy (y) by urban rate of population (x) for those alcconsumption <= 10
            alcconsumption  lifeexpectancy  urbanrate  c_alcconsumption
c_urbanrate                                                            
(0, 40]            3.637647       60.787235  27.251373                 0
(40, 70]           4.734600       68.791480  55.665200                 0
(70, 100]          5.192424       75.887818  83.690909                 0
means for life expectancy (y) by urban rate of population (x) for those alcconsumption >10
            alcconsumption  lifeexpectancy  urbanrate  c_alcconsumption
c_urbanrate                                                            
(0, 40]           12.812500       66.794500  27.125000                 1
(40, 70]          14.360455       73.006773  59.404545                 1
(70, 100]         13.060000       78.246250  80.318750      

Conclusion: even we took  alcconsumption as moderator,both the anova models are statistically significant that is life expectancy (y) depends on  urban rate of population (x) for those alcconsumptionn<=10 and life expectancy (y) depends on  urban rate of population (x) for those alcconsumptionn >10. Also  means of lifeexoectancy for the two groups giving the same results as the yielded with out the moderator.

Code
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
#worked" convert to numeric as python read data as object(string)
data1['lifeexpectancy’]=pandas.to_numeric(data1['lifeexpectancy’], errors='coerce’)
data1['urbanrate’]=pandas.to_numeric(data1['urbanrate’], errors='coerce’)
data1.dtypes
# calculation of centre and spread
summary1=data1['lifeexpectancy’].describe()
print(summary1)
summary2=data1['urbanrate’].describe()
print(summary2)
## for ANOVA make explanatory-urbanrate into into four categorical
data1['c_urbanrate’]=pandas.cut(data1.urbanrate,[0,40,70,100])
#drop nan and make sub set
sub1=data1.dropna(subset=['lifeexpectancy’,'urbanrate’])
sub2=sub1.copy()
print(len(sub2))
#frequency
gf2=sub2.groupby('c_urbanrate’).size()
print(gf2)
gp2=sub2.groupby('c_urbanrate’).size()*100/len(sub2)
print(gp2)
# using ols function for calculating the F-statistic and associated p value
model1 = smf.ols(formula='lifeexpectancy ~ C(c_urbanrate)’, data=sub2)
results1 = model1.fit()
print (results1.summary())
# comment: From ANOVA:As the p-value almost 0 we reject H0 and conclude that life expectancy (y) depends urban rate of population(x)
# that is means life expectancy of four urban groups are not eual
# we have conduct mutiple comparison  test:post hoc paired comparisons-tukeyhsd
mct1 = multi.MultiComparison(sub2['lifeexpectancy’], sub2['c_urbanrate’])
rest1 = mct1.tukeyhsd()
print(rest1.summary())
#
# Moderator-alcconsumption
data1['alcconsumption’]=pandas.to_numeric(data1['alcconsumption’], errors='coerce’)
summary3=data1['alcconsumption’].describe()
print(summary3)
# cut alcconsumptioninto two groups upto 10 and more than 10
data1['c_alcconsumption’]=pandas.cut(data1.alcconsumption,[0,10,25])
gf3=data1.groupby('c_alcconsumption’).size()
print(gf3)
gp3=data1.groupby('c_alcconsumption’).size()*100/len(data1)
print(gp3)
#drop nan and make sub set
sub3=data1.dropna(subset=['lifeexpectancy’,'c_urbanrate’, 'c_alcconsumption’])
sub4=sub3.copy()
print(len(sub4))
##convert  c_alcconsumption to category 0 and 1 as follows
sub4['c_alcconsumption’]=sub4.c_alcconsumption.astype('category’).cat.codes
gf4=sub4.groupby('c_alcconsumption’).size()
print(gf4)
## make another two subgroups
sub41=sub4[(sub4['c_alcconsumption’]==0)]
sub42=sub4[(sub4['c_alcconsumption’]==1)]
print(len(sub41))
print(len(sub42))
## run two ANOVA for two groups
print ('association between life expectancy (y) and urban rate of population (x) for those alcconsumptionn<=10’)
model2 = smf.ols(formula='lifeexpectancy ~ C(c_urbanrate)’, data=sub41)
results2 = model2.fit()
print (results2.summary())
print ('association between life expectancy (y) and urban rate of population (x) for those alcconsumption > 10’)
model3 = smf.ols(formula='lifeexpectancy ~ C(c_urbanrate)’, data=sub42).fit()
print (model3.summary())
print ('means for life expectancy (y) by urban rate of population (x) for those alcconsumption <= 10’)
m3= sub41.groupby('c_urbanrate’).mean()
print (m3)
print ('means for life expectancy (y) by urban rate of population (x) for those alcconsumption >10’)
m4 = sub42.groupby('c_urbanrate’).mean()
print (m4)

