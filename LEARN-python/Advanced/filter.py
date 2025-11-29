list1=[1,2,3,4,5,6,7,8,9,10]
def even(x):
    if x%2==0:
        return x
    else:
        return 0
f=filter(even,list1)
print("using normal fn: ", list(f)) # convert a filter object to a list

# using lambda fn
f=filter(lambda x:x%2==0,list1)
print("using lambda fn: ", list(f))
