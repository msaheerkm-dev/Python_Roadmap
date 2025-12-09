# unique values from a list
lst=[1,2,4,3,3,2,5,7,5,3,9,0,2,1,3]
uniq_lst=[]

for i in lst:
    if i not in uniq_lst:
        uniq_lst.append(i)
print(uniq_lst) 