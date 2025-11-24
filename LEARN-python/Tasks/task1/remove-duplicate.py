list=[1,3,2,6,4,2,3,7,3,5,8,9]
print("list: ",list)
# simplest way
print("unique list: ",set(list))
# using loop
unique_list=[]
duplicate=set(list)
for item in list:
    if item not in unique_list:
        unique_list.append(item)
    else:
        print(f"{item} repeated in the original list")
print("unique_list: ",unique_list)
set={1,3,2,6,4,2,3,7,3,5,8,9}
print("set: ",set)
