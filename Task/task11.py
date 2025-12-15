# sort without using sort()
list=[3,5,2,1,7,8,0,9,4,6]
for i in range(len(list)):
    for j in range(len(list)):
        if list[i]<list[j]:
            list[i],list[j]=list[j],list[i]
print(list)