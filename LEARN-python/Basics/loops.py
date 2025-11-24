a=10
while a<=50 :#while loop
    print(a)
    a=a+2
else :
    print('loop finished')

print('\n')

lists=['malayalam.txt','english.txt','hindi.txt','spanish.txt']
for i in lists :# for loop
    print(i)
    print(i[0:-4])# slicing in for loop

print('\n')

for i in range(5,50,5) :
    print(i)