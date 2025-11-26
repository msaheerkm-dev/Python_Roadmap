""" important point there are 3 data structures in pandas library
1.series = 1D - list,tuple,dictionary,set
2.dataframe = 2D - nested list , nested dictionary , data_set
3.panel = 3D
"""

import pandas as pd

# nested list(list inside another list) 
a=[[1,'raju',10000,'IT'],
   [2,'ramu',12000,'MED'],
   [3,'rajan',13000,'IT'],
   [4,'rajesh',14000,'MED'],
   [5,'renjith',15000,'IT']]
print(a)
df=pd.DataFrame(a) # convert the above nested list into a data frame
print(df)
print(df.columns)
df.columns=['id','name','salary','field'] # to add column head to the nested list
df=df.drop(columns="name")# to drop a column from the data frame
df.rename(columns={"id":"ID"}) # to rename a column name in a dataframe
print(df.sort_values()) # sort by coloumn values
print(df.sort_index()) # sort by index rows
print(df['id'].value_counts()) # to count values
print(df['id'].unique()) # for unique values
df.at[1, 'salary'] = np.nan # insert null values inside a dataframe
df=df.fillna(0) # fill the null value inside a dataframe with a specified value
df=df.replace(10000,12345) # to replace the values inside a dataframe
df['salary']=df['salary'].astype(int) # to change datatype
print(df[df['salary']>13000]) # filtering the values(single condition)
print(df[(df['salary']>13000) & (df['salary']<15000)]) # filtering the values(multiple condition)
print(df[df['id'].between(2,4,inclusive='both')]) # between fn
print(df.query('salary> 12000 and salary < 15000')) # filteing using query
df2=df.set_index('id') # it set the given column as index
df2.reset_index(inplace=True) # it resets the index back to normal (inplace directly modify the dataframe)
df2=df2.reindex(range(10),fill_value=0)# extend the index upto 9
print(df['salary'].idxmax()) # return the index of the maximin value
print(df['salary'].idxmax()) # return the index of the minimum value
print(df.nlargest(3,'salary')) #return the largest 3 salary from the salary
print(df.nsmallest(3,'salary')) #return the smallest 3 salary from the salary
print(df.loc[1:2,'name':'salary']) # SLICE LABELS

#conditional assignment
df['result']='low paying'
df.loc[df['salary']>13000, 'result']='high paying'
print(df)
print('\n')

# where and mask
print(df['salary'].where(df['salary']>13000,0)) # where replace values when condition is false with 0
print(df['salary'].mask(df['salary']>13000,0)) # mask replace values when condition is true with 0
# mask is the opposite of where

# nested dictionary (dictionary inside another dictionary)
dict={
    'id':[1,2,3,4,5],
    'name':['raju','ramu','rajan','rajesh','renjith'],
    'salary':[10000,12000,13000,14000,15000],
    'field':['IT','MED','IT','MED','IT']
}
print(dict)
df=pd.DataFrame(dict)
print(df)
print(df.describe()) # to summarize the integers in the dictionary only int
print(df.describe(include='O')) # it summarize the string values in the dictionary
print(df.describe(include='all'))# it summarize all the string and integer values in the dictionary
print(df.dtypes)
df['experince']=['1','4','5','3','2'] # to add new column to the nested dictionary
print(df)
print('\n')

# pandas to load data from an external file
data=pd.read_csv('venv\LEARN-python\Python-Library\pandas\data_1.csv',sep=',',header=None)
data.columns=['id','name','salary','company','place']
print(data)
print(data.isna().sum()) # it returns the empty items in the data isna() fn
data=data.fillna('updating') # it fills anything in the empty places
print(data)
data=data.rename(columns={'id':'UID'}) # rename() fn is used to rename a col
print(data)
df1=data.iloc[:,3] # iloc fn is used to print required values from the data according to the index value slicing is possible
print(df1)
print('\n')

# loc() fn is used to filter the data
a=[[1,'raju',15000,'IT'],
   [2,'ramu',12000,'MED'],
   [3,'rajan',10000,'IT'],
   [4,'rajesh',14000,'MED'],
   [5,'renjith',11000,'IT']]
df1=pd.DataFrame(a)
df1.columns=['id','name','salary','field'] # to add column head to the nested list
print(df1)
df2=df1[['id','name']]
print(df2)
df3=df1.loc[df1['salary']>13000] [['id', 'name']]# it retrieves the data with the salary is greater than 13000 single condition
print(df3)
df4=df1.loc[(df1['salary']>12000)&(df1['salary']<15000)]
print(df4)
print('\n')

# sort
df5=df1.sort_values(by='salary') # ascending order
print(df5)
df6=df1.sort_values(by='salary',ascending=False) # ascending order
print(df6)
print('\n')

 # drop functions(drop(), drop_ duplications())
data=pd.read_csv('venv\LEARN-python\Python-Library\pandas\data_1.csv',sep=',',header=None)# usecols fn in used to use specified columns
data.columns=['id','name','salary','company','place']
print(data)
df1=data.drop_duplicates() # to avoid data redundancy it is used to remove duplicate rows
print(df1)
df2=data.drop(columns='place') # it removes a column form the data frame\
# df2=data.drop(['place'],axis=1)
print(df2)
print('\n')

# evaluating functions are count,sum , min , max , mean
df3=data.groupby('salary') ['salary'].count().sort_values()
print(df3)
df3=data.groupby('salary') ['salary'].sum() # it sums the repeated values in the data frame
print(df3)
df3=data.groupby('salary') ['salary'].min() 
print(df3)
df3=data.groupby('salary') ['salary'].max() 
print(df3)
df3=data.groupby('salary') ['salary'].mean() 
print(df3)
print('\n')

# joins concept there are 4 types of joins
# inner join , outer join , left join , right join
d1={
    'id':[1,2,3,4,5],
    'name':['raju','ramu','rajan','rajesh','renjith'],
    'field':['IT','MED','IT','MED','IT']
}
print(d1)
df1=pd.DataFrame(d1)
print(df1)
d2={
    'id':[1,2,3,4,5],
    'salary':[10000,12000,13000,14000,15000],
}
print(d2)
df2=pd.DataFrame(d2)
print(df2)
# inner join
inner_join=pd.merge(df1,df2,on='id',how='inner')
print(inner_join)
print("-"*50)
# outer join
outer_join=pd.merge(df1,df2,on='id',how='outer')
print(outer_join)
print("-"*50)
# right join (return all values corresponding to the right side data frame)
right_join=pd.merge(df1,df2,on='id',how='right')
print(right_join)
print("-"*50)
# left join (print all values corresponding to the left side data frame)
left_join=pd.merge(df1,df2,on='id',how='left')
print(left_join)
print("-"*50)

# replacing null values cell by cell
import numpy as np
a=[[1,'raju',15000,'IT'],
   [2,'ramu',12000,'MED'],
   [3,'rajan',10000,'IT'],
   [4,'rajesh',14000,'MED'],
   [5,'renjith',11000,'IT']]
df1=pd.DataFrame(a)
df1.columns=['id','name','salary','field'] # to add column head to the nested list
print(df1)
print("-"*50)
df1['place']=['kolkata','chennai','mumbai','kochi','calicut']
df1['experiance']=[4,3,6,5,3]
print(df1)
print("-"*50)
df1.at[1,'experiance']=np.nan
df1.at[2,'place']=np.nan
df1.at[3,'field']=np.nan
df1.at[4,'salary']=np.nan
print(df1)
print("-"*50)
df1.at[1,'experiance']=5
df1.at[2,'place']='banglore'
df1.at[3,'field']='MED'
df1.at[4,'salary']=13000
print(df1)
print("-"*50)
df1.loc[[1,3],['experiance']]=np.nan
df1.loc[[0,2],['place']]=np.nan
print(df1)
print("-"*50)
experiance={1:5,3:7}
place={0:'kolkata',2:'banglore'}
for index,values in experiance.items():
    df1.at[index,'experiance']=values
for index,values in place.items():
    df1.at[index,'place']=values
print(df1)
# Single loop to update
updates = {
    0: {'place': 'kolkata'},
    1: {'experience': 5},
    2: {'place': 'bangalore'},
    3: {'experience': 7}
}
for index, changes in updates.items():
    for column, value in changes.items():
        df1.at[index, column] = value
print(df1)
print('-'*30)

# concat
d1={
    'id':[1,2,3,4,5],
    'name':['raju','ramu','rajan','rajesh','renjith'],
}
df1=pd.DataFrame(d1)
print(df1)
d2={
    'id':[1,2,3,4,5],
    'name':[20,24,21,26,27],
}
df2=pd.DataFrame(d2)
print(df2)
print('-'*30)
ct=pd.concat([df1,df2],axis=1) # horizontal concat
print(ct)
print('-'*30)
ct1=pd.concat([df1,df2],ignore_index=True) # vertical concat with no repetation of index values
print(ct1)
print('-'*30)
ct2=pd.concat([df1,df2],keys=['name','age']) # vertical concat seperated by keys
print(ct2)
print('-'*30)
salary=pd.Series([10000,13000,14000,12300,14300],name='salary')
ct3=pd.concat([df1,salary])
print(ct3)
print('-'*30)

# merge()
mg=pd.merge(df1,df2,on='id',suffixes=('_left','_right'),how='inner',indicator=True) # merging 2 data frame values of how (inner,outer,left,right)
print(mg)
print('-'*30)

# melt()
mlt=pd.melt(df1,id_vars='id',var_name='x',value_name='y') # detailed view of a data frame
print(mlt)
print('-'*30)

# crosstab()
ct=pd.crosstab(df1.name,df1.id,margins=True)
print(ct)
print('-'*30)

# correlation
dd={
    'id':[1,2,3,4,5],
    'age':[20,23,25,21,20]
}
dd1=pd.DataFrame(dd)
cr=dd1.select_dtypes(['number']).corr() # select_dtypes() helps to select particular datatype from the dataframe
print(cr)

# overlaying index aligning by index
s1=pd.Series([1,2,3],index=['a','b','c'])
s2=pd.Series([1,2,3],index=['b','c','d'])
result=s1+s2
print(result)
# isin membership df[df.col.isin(['a','b'])]

#aggregation and groupby
data = {
    'Team': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Player': ['P1', 'P2', 'P3', 'P4', 'P5', 'P6'],
    'Score': [10, 20, 15, 25, 30, 40]
}
df = pd.DataFrame(data)
print(df)
print(df.groupby('Team')['Score'].sum())
result=df.groupby('Team')['Score'].agg(total='sum',minimum='min',maximum='max',mean='mean')
print(result)

# Group by multiple keys (class and subject) and aggregate
data = {
    'class': ['A','A','A','B','B','B'],
    'subject': ['Math','Math','Science','Math','Science','Science'],
    'marks': [80, 90, 75, 60, 70, 85]
}

df = pd.DataFrame(data)

result = df.groupby(['class','subject'])['marks'].agg(['sum','mean','max'])
print(result)

# transform() fn similar t agg()
data = {'id': [1,1,2,2,3,3],
        'score': [10, 20, 15, 25, 30, 35]}

df = pd.DataFrame(data)
# instead of summarizing one value per group it return the same size as the original dataframe/series
# Using transform: calculate mean per group
df['mean_score'] = df.groupby('id')['score'].transform('mean')
print(df)



# pivot table used to summarize and organise dataframe
data = {
    'class': ['A','A','A','B','B','B'],
    'subject': ['Math','Science','Math','Math','Science','Science'],
    'marks': [80, 75, 90, 60, 70, 85]
}

df = pd.DataFrame(data)

# Pivot table: average marks by class and subject
pivot = pd.pivot_table(df, values='marks', index='class', columns='subject', aggfunc='mean')
print(pivot)

# crosstab is used to count the repeated values in the df
data = {
    'class': ['A','A','B','B','B','C'],
    'subject': ['Math','Science','Math','Science','Science','Math']
}

df = pd.DataFrame(data)

# Crosstab: count of subjects per class
result = pd.crosstab(df['class'], df['subject'])
print(result)
