tuple=(0,1,2,3,4)
print("tuple:",tuple)
tuple2=(5,6,7,8,9)
print("second tuple: ",tuple2)
tuple3=tuple.__add__(tuple2)
# tuple3=tuple+tuple2
print("appended tuple: ",tuple3)

for i in tuple:
    print(i)

print(len(tuple))