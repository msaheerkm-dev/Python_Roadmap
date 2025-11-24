# oop's concept constructor
class PersonData:
    year=2025
    def __init__(self,name,age,place): # constructor
        self.name=name
        self.age=age
        self.place=place
    def add_age(self):
        self.age=self.age+1
    def relocate(self,new_place):
        self.place=new_place
    def display(self):
        print('year :', PersonData.year)
        print('name :'+self.name)
        print('age :'+str(self.age))
        print('place :'+self.place)
    @classmethod
    def add_year(cls):
        PersonData.year=PersonData.year+1
    @staticmethod # value doesnt change
    def welcome():
        print('welcome all')
x=PersonData('saheer',20,'kerala') # the constructor works at the time of the object creation
y=PersonData('ronaldo',40,'potugal')
x.display()
y.display()
x.add_age()
x.relocate('dubai')
y.add_age()
y.relocate('brazil')
PersonData.welcome()
PersonData.add_year()
x.display()
y.display()