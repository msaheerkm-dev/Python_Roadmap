# important note set is unordered and unindexed it contains unique elements
set1={1,2,3,4,5}
print(set1)
for i in set1:
    print(i)
print(1 in set1) #check if 1 exist in set1 it will return true
set1.add(6) #add 6 to set1
print(set1)
set1.remove(2) #remove 2 from set1
print(set1)
set1.discard(3) #discard 3 from set1 if 3 doesn't exist it won't raise an error
print(set1)
set1.update({7,8,9}) #update set1 with new elements
print(set1)