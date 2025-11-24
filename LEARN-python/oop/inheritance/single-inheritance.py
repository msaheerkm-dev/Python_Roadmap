# inheritance in python oop's concept
class BaseClass:
    def __init__(self):
        print('base class')
    def set_name(self,n):
        self.name=n
        print('base class name')
    def display_name(self):
        print('name is '+self.name)
class SubClass(BaseClass):
    def __init__(self): # constructor overriding
        super().__init__()
        # print('sub class')
    def set_name(self,n):# method overriding
        super().set_name(n)
        # self.name=n
        print('sub class name') 
    def welcome(self):
        print('welcome')
x=BaseClass()
x.set_name('hulk')
x.display_name()
y=SubClass()
y.welcome()
y.set_name('iron man')
y.display_name() # inherited from the BaseClass