import pandas as pd
 
 # series 1D data structure
a=pd.Series([1,2,3,4,5,6])
print(a)
print(type(a))
print(a.shape)
print(a.size)
print(a.dtype)
print('\n')

# looping in series
a=pd.Series([ i for i in range(5,50,5)])
print(a)
print('\n')

# append to series using append() fn
a=pd.Series([1,2,3,4,5,6])
b=pd.Series([7,8,9,10,11,12])
c=a._append(b,ignore_index=True) # ignore__index is used for the condinuation of index numbers else it print diff index
print(c)
print('\n')

# convert dictionary to series
a={1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E'}
print(a)
b=pd.Series(a) # the index number of the series is the key values from the dictionary
print(b)
print('\n')

# set default data type of a series
a=pd.Series([1,2,3,4,5,6],dtype=float)
print(a)
print('\n')

# in pandas index of the series can be change by using index keyword the 
# if the positon of the series changed but it's value will not change
a=pd.Series([1,2,3,4,5,6],dtype=float,index=['a','b','c','d','e','f'])
print(a)
print('\n')

# mathematical operations in series 
a=pd.Series([1,2,3,4,5,6])
b=pd.Series([7,8,9,10,11,12])
ad=a.add(b)
print(ad)
sb=a.sub(b)
print(sb)
dv=a.div(b)
print(dv)
ml=a.mul(b)
print(ml)
print('\n')