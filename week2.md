# Python-Data-analysis-tools
## week 2 assignment: chi square test
import pandas
import numpy
import scipy.stats
import seaborn
import matplotlib.pyplot as plt
# read data ‘nesarc in python
data1=pandas.read_csv('my_nesarc.csv’, low_memory=False)
#worked" convert to numeric as python read data as object(string)
data1['S2DQ1’]=pandas.to_numeric(data1['S2DQ1’], errors='coerce’)
data1['S2AQ3’]=pandas.to_numeric(data1['S2AQ3’], errors='coerce’)
data1['MARITAL’]=pandas.to_numeric(data1['MARITAL’], errors='coerce’)
data1.dtypes
Out[8]:
Unnamed: 0        int64
ETHRACE2A         int64
ETOTLCA2         object
IDNUM             int64
PSU               int64
HER12ABDEP        int64
HERP12ABDEP       int64
OTHB12ABDEP       int64
OTHBP12ABDEP      int64
NDSymptoms      float64
Length: 3010, dtype: object
#replacing missing values for nan (ALSO 9 OR 99 CONSIDERING MISSING)
print('count for original S2DQ1’)
count for original S2DQ1
f1=data1['S2DQ1’].value_counts(sort=False,dropna=False)
print(f1)
1     8124
2    32445
9     2524
Name: S2DQ1, dtype: int64
print('count for S2DQ1 by replacing missing with nan’)
count for S2DQ1 by replacing missing with nan
data1['S2DQ1’]=data1['S2DQ1’].replace(9, numpy.nan)
f11=data1['S2DQ1’].value_counts(sort=False, dropna=False)
print(f11)
1.0     8124
2.0    32445
NaN     2524
Name: S2DQ1, dtype: int64
print('count for original S2AQ3’)
count for original S2AQ3
f2=data1['S2AQ3’].value_counts(sort=False,dropna=False)
print(f2)
1    26946
2    16116
9       31
Name: S2AQ3, dtype: int64
print('count for S2AQ3 by replacing missing with nan’)
count for S2AQ3 by replacing missing with nan
data1['S2AQ3’]=data1['S2AQ3’].replace(9,numpy.nan)
f22=data1['S2AQ3’].value_counts(sort=False, dropna=False)
print(f22)
2.0    16116
1.0    26946
NaN       31
Name: S2AQ3, dtype: int64
print('count for original MARITAL’)
count for original MARITAL
f3=data1['MARITAL’].value_counts(sort=False,dropna=False)
print(f3) # no missing values
1    20769
2     1312
3     4271
4     5401
5     1445
6     9895
Name: MARITAL, dtype: int64
# select rows: subset of data1 given that FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER’
sub1=data1[(data1['S2DQ1’]==1)]
sub2=sub1[['MARITAL’,'S2AQ3’]]
8124
sub3=sub2.dropna()
print(len(sub3))
8123
#frequency
f4=sub3['S2AQ3’].value_counts()
print(f4)
1.0    5544
2.0    2579
Name: S2AQ3, dtype: int64
f5=sub3['MARITAL’].value_counts()
print(f5)
1    3837
6    1871
4    1263
3     470
2     351
5     331
Name: MARITAL, dtype: int64
# contingency table of observed counts
cto=pandas.crosstab(sub3['S2AQ3’], sub3['MARITAL’], margins=True)
print (cto)
MARITAL     1    2    3     4    5     6   All
S2AQ3                                        
1.0      2571  274  206   869  216  1408  5544
2.0      1266   77  264   394  115   463  2579
All      3837  351  470  1263  331  1871  8123
# column percentages
colsum=cto.sum(axis=0)
colpt=cto/colsum
MARITAL         1         2         3         4         5         6       All
S2AQ3                                                                        
1.0      0.335027  0.390313  0.219149  0.344022  0.326284  0.376269  0.341253
2.0      0.164973  0.109687  0.280851  0.155978  0.173716  0.123731  0.158747
All      0.500000  0.500000  0.500000  0.500000  0.500000  0.500000  0.500000
print(colpt)
# chi-square
print ('chi-square value, p value, expected counts’)
chi-square value, p value, expected counts
cs1= scipy.stats.chi2_contingency(cto)
print (cs1)
(191.58929962177555, 1.7679125907777407e-34, 12, array([[2618.77729903,  239.55976856,  320.77803767,  862.00566293,
        225.9096393 , 1276.96959252, 5544.        ],
      [1218.22270097,  111.44023144,  149.22196233,  400.99433707,
        105.0903607 ,  594.03040748, 2579.        ],
      [3837.        ,  351.        ,  470.        , 1263.        ,
        331.        , 1871.        , 8123.        ]]))
Conclusion: as the p value is very small we can conclude that  drinking alchole depend on marital status who have family history of drinking (FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER)
For chi square we do not need need to run post hoc paired comparisons test

Python code
#w2 assignment: chi square test
# research question: whether drinking alchole depend on marital status who have family history of drinking
#load the libries
import pandas
import numpy
import scipy.stats
import seaborn
import matplotlib.pyplot as plt
# read data 'nesarc in python
data1=pandas.read_csv('my_nesarc.csv’, low_memory=False)
print(len(data1))
#all columns upper case
data1.columns=map(str.upper,data1.columns)
#data type
data1.dtypes
#worked" convert to numeric as python read data as object(string)
data1['S2DQ1’]=pandas.to_numeric(data1['S2DQ1’], errors='coerce’)
data1['S2AQ3’]=pandas.to_numeric(data1['S2AQ3’], errors='coerce’)
data1['MARITAL’]=pandas.to_numeric(data1['MARITAL’], errors='coerce’)
data1.dtypes
#replacing missing values for nan (ALSO 9 OR 99 CONSIDERING MISSING)
print('count for original S2DQ1’)
f1=data1['S2DQ1’].value_counts(sort=False,dropna=False)
print(f1)
print('count for S2DQ1 by replacing missing with nan’)
data1['S2DQ1’]=data1['S2DQ1’].replace(9, numpy.nan)
f11=data1['S2DQ1’].value_counts(sort=False, dropna=False)
print(f11)
print('count for original S2AQ3’)
f2=data1['S2AQ3’].value_counts(sort=False,dropna=False)
print(f2)
print('count for S2AQ3 by replacing missing with nan’)
data1['S2AQ3’]=data1['S2AQ3’].replace(9,numpy.nan)
f22=data1['S2AQ3’].value_counts(sort=False, dropna=False)
print(f22)
print('count for original MARITAL’)
f3=data1['MARITAL’].value_counts(sort=False,dropna=False)
print(f3) # no missing values
# select rows: subset of data1 given that FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER’
sub1=data1[(data1['S2DQ1’]==1)]
print(len(sub1))
# drop na values
#sub2=sub1.dropna()
#also drop nan and make another sub set
sub2=sub1[['MARITAL’,'S2AQ3’]]
sub3=sub2.dropna()
print(len(sub3))
#frequency
f4=sub3['S2AQ3’].value_counts()
print(f4)
f5=sub3['MARITAL’].value_counts()
print(f5)
# contingency table of observed counts
cto=pandas.crosstab(sub3['S2AQ3’], sub3['MARITAL’], margins=True)
print (cto)
# column percentages
colsum=cto.sum(axis=0)
colpt=cto/colsum
print(colpt)
# chi-square
print ('chi-square value, p value, expected counts’)
cs1= scipy.stats.chi2_contingency(cto)
print (cs1)

