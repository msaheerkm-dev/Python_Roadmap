limit=int(input('Enter the limit: '))

a,b=0,1
for i in range(limit):
    print(a)
    a,b=b,a+b
