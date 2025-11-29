arr=[]
n=int(input("enter how many elements do you want to enter: "))
for i in range(n):
    element=int(input("enter the element- "))
    arr.append(element)
print("array :",arr)
# inbuild method
print("reversed array :",arr[::-1])    
# using for loop
rev=[]
for i in range(len(arr)):
    rev.append(arr[-(i+1)])
print("reversed array :",rev)