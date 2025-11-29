# operator overloading
class sample:
    def set_name(self,n):
        self.name=n
    def __add__(self,other):
        n=self.name+" "+other.name
        return n
first_name=sample()
second_name=sample()
first_name.set_name('iron')
second_name.set_name('man')
full_name=first_name+second_name
print(full_name)