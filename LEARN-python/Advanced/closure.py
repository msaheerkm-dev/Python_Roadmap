'''
closure concept executig an inner fn( nested fn ) outside the scope 
it is a fn object that remembers the values in the enclosing scope 
even afer they are not present in the memory
'''
def outer():
    a=10
    def inner():
        b=10
        sm=a+b
        return sm
    return inner
x=outer() # here x is act as inner fn
print(x.__name__) # it is inner
print(x())
