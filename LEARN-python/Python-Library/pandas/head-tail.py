import pandas as pd

a=pd.Series([ i for i in range(5,50,5)])
# print first n elements using head() fn
print(a.head(7)) # by default it will print first 5 elements 
print('\n')

# print last n elements using tail() fn
print(a.tail(7)) # by default it will print first 5 elements 
print('\n')