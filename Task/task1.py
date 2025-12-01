# sum of digits of a number
num=int(input('enter a number..'))
total=0
while(num>0):
    d=num%10
    total=total+d
    num=int(num/10)
print(total)

# optimal code
print(sum(int(d) for d in input("Enter a number: ")))

