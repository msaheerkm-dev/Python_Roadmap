#each object obtain diff memory space
class MySampleClass:
    def hello(self,n): 
        self.name=n
    def print_name(self):
        print(self.name)
x=MySampleClass() 
y=MySampleClass() 
name='saheer'
x.hello(name)
x.print_name()
y.hello('ronaldo')
y.print_name()