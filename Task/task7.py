# sort
lst=[3,4,5,2,7,8,9]
# new_lst=sorted(lst,reverse=True)
# print(new_lst[1])

# without sort
big=max(lst)
rem=[x for x in lst if x!= big]
second_larg=max(rem)
print(second_larg)