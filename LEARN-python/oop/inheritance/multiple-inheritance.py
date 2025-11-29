# multiple inheritance
class First:
    def display_first(self):
        print('first class')
class Second:
    def display_Second(self):
        print('Second class')
class Third(First,Second):
    def display_Third(self):
        print('Third class')
x=Third()
x.display_first()
x.display_Second()
x.display_Third()