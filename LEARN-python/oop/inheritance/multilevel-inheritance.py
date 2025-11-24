# multilevel inheritance 
# if the classes condains multiple methods with same class and th object call the fn name the first catching fn will be treated as first
class First:
    def display_first(self):
        print('first class')
class Second(First): # inherit first class
    def display_Second(self):
        print('Second class')
class Third(Second): # inherit second class
    def display_Third(self):
        print('Third class')
x=Third()
x.display_first()
x.display_Second()
x.display_Third()
print(Third.mro()) # it shows the priority of the inherited classes (method resolution order) MRO