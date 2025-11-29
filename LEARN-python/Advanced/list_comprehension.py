'''
list comprehension is advance way of filtering 
the main list to create another list with simple synthax
'''
name=input("enter the names: ").split()
#name=list(input("enter the name: ")) used to create list from single name
print("names:",name)
# it is used to print the 0 indexed element from each item from the name
l=[n[0] for n in name] 
print(l)
# this comprehension is used to print the entire character from the first name
l=[ch for ch in name[0]]
print(l)