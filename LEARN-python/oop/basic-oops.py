# oop's concept in python (object orieted programming)
class MySampleClass:
    def hello(self,n): # x object is passed as the parameter in the fn hello as self( self is default name but we can set any name instead of it )
        print('hello '+n)
x=MySampleClass() # created a object
name='saheer'
x.hello(name) # MysampleClass.hello(x) this is what it is look like