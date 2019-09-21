# Python-Data-analysis-tools
## w3 assignment: correlation coefficient
import pandas
import numpy
import seaborn
import scipy
import matplotlib.pyplot as plt
data1=pandas.read_csv(‘data_gapminder.csv’, low_memory=False)
print(len(data1))
213
#all columns upper case
#data1.columns=map(str.upper,data1.columns)
#data type
data1.dtypes
Out[7]:
country                 object
incomeperperson         object
alcconsumption          object
armedforcesrate         object
breastcancerper100th    object
co2emissions            object
femaleemployrate        object
hivrate                 object
internetuserate         object
lifeexpectancy          object
oilperperson            object
polityscore             object
relectricperperson      object
suicideper100th         object
employrate              object
urbanrate               object
dtype: object
#set pandas to to show all columns
pandas.set_option('display.max_columns’, None)
#set pandas to to show all rows
pandas.set_option('display.max_rows’, None)
# response is lifeexpectancy and explanatory variablevariable is urbanrate
#worked" convert to numeric as python read data as object(string)
data1['lifeexpectancy’]=pandas.to_numeric(data1['lifeexpectancy’], errors='coerce’)
data1['urbanrate’]=pandas.to_numeric(data1['urbanrate’], errors='coerce’)
data1.dtypes
Out[16]:
country                  object
incomeperperson          object
alcconsumption           object
armedforcesrate          object
breastcancerper100th     object
co2emissions             object
femaleemployrate         object
hivrate                  object
internetuserate          object
lifeexpectancy          float64
oilperperson             object
polityscore              object
relectricperperson       object
suicideper100th          object
employrate               object
urbanrate               float64
dtype: object
#drop nan and make sub set
sub1=data1.dropna(subset=['lifeexpectancy’,'urbanrate’])
sub2=sub1.copy()
print(len(sub2))
188
#scatter plot
scat1 = seaborn.regplot(x='urbanrate’, y='lifeexpectancy’, fit_reg=True, data=sub2)
plt.xlabel('Urban Rate’)
plt.ylabel('life Expectancy’)
plt.title('Scatterplot for the Association Between Urban Rate and life Expectancy’)

 


Out[22]: Text(0.5, 1.0, 'Scatterplot for the Association Between Urban Rate and life Expectancy’)
￼
print ('association between urbanrate and life Expectancy’)
association between urbanrate and life Expectancy
print (scipy.stats.pearsonr(sub2['urbanrate’], sub2['lifeexpectancy’]))
(0.6187071046244896, 3.028137554379085e-21)
# conclusion: it is observed that the correlatiion between life expectancy (y) and urban rate of population (x)  is positive and modeately strong (r=0.62)
# increase ( or decrease ) in urban rate of population (x) also increase ( or decrease ) in life expectancy (y) and  
# as the p-value is very small, the relationship is statistically significant


Python code:
#load the libries
import pandas
import numpy
import seaborn
import scipy
import matplotlib.pyplot as plt
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
#drop nan and make sub set
sub1=data1.dropna(subset=['lifeexpectancy’,'urbanrate’])
sub2=sub1.copy()
print(len(sub2))
#scatter plot
scat1 = seaborn.regplot(x='urbanrate’, y='lifeexpectancy’, fit_reg=True, data=sub2)
plt.xlabel('Urban Rate’)
plt.ylabel('life Expectancy’)
plt.title('Scatterplot for the Association Between Urban Rate and life Expectancy’)
#
print ('association between urbanrate and life Expectancy’)
print (scipy.stats.pearsonr(sub2['urbanrate’], sub2['lifeexpectancy’]))

