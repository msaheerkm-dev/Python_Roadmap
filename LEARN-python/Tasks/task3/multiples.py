n=int(input ("enter the limit: "))
sum=0
for i in range(1,n):
    if i%3==0 or i%5==0:
        print(i)
        sum+=i
print(sum)    
