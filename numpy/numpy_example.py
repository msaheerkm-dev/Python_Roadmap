import numpy as np

#numpy array(1D)
a=np.array([1,2,3,4,5])
print('1D array')
print(a)
print('type :',type(a))# to find type
print('dimention: ',a.ndim)# to find dimention of array
print('size: ',a.size)# to find no of elements of the matrix
print('\n')

# 2D array
b=np.array([[1,2],[3,4],[5,6]],dtype=float)
print('2D array')
print(b)
print('dimention: ',b.ndim)# to find dimention of array
print('order: ',b.shape)# to find order of the array
print('size: ',b.size)# to find no of elements of the matrix
print('type: ',b.dtype)# to find type of elements in the matrix
print(b[:,1])#accessing colum
b=b.transpose()# transpose() fn is used to transpose a matrix
print('transpose',b) 
print('\n')

# 3d array
c=np.array([[[1,2,3],[4,5,6]]])
print('3D array',)
print(c)
print('dimention: ',c.ndim)# to find dimention of array
print('order: ',c.shape)# to find order of the array
print('size: ',c.size)# to find no of elements of the matrix
print('type: ',c.dtype)# to find type of elements in the matrix
print('\n')

# zero matrix (by default other than array in numpy has float type)
d=np.zeros([7])# 1D zero matrix
print(' 1D zero matrix')
print(d)
d=np.zeros([3,4])# 2D zero matrix
print(' 2D zero matrix')
print(d)
d=np.zeros([2,4,3])# 3D zero matrix
print(' 3D zero matrix')
print(d)
print('\n')

# one matrix (by default other than array in numpy has float type)
d=np.ones([7])# 1D one matrix
print(' 1D one matrix')
print(d)
d=np.ones([3,4])# 2D one matrix
print(' 2D one matrix')
print(d)
d=np.ones([2,4,3])# 3D one matrix
print(' 3D one matrix')
print(d)
print('\n')

# full matrix (by default other than array in numpy has float type)
d=np.full([7],fill_value=10)# 1D full matrix
print(' 1D full matrix')
print(d)
d=np.full([3,4],fill_value=10)# 2D full matrix
print(' 2D full matrix')
print(d)
d=d.reshape([4,3])# reshape() fn is used to change the order of the matrix
print('reshaped 2D full matrix')
print(d)
d=np.full([2,3,5],fill_value=10)# 3D full matrix
print(' 3D full matrix')
print(d)
d=d.reshape([2,5,3])# reshape() fn is used to change the order of the matrix (important note : size must be same)
print('reshaped 3D full matrix')
print(d)
d=d.flatten()# flatten() fn is used to convert 2D/3D to 1D (important note : size must be same)
print('flatten 3D full matrix to 1D  matrix')
print(d)
print('\n')

# identity matrix (square matrix) also we can use eye() fn instead of using identity() fn
e=np.identity(7)
print(' identity matrix')
print(e)
print('\n')

# arange() fn 
f=np.arange(11)# it arange o-10 in an array
print(f)
print("arange 5-52 numbers in an array and also increment by 2")
f=np.arange(5,52,2).reshape([8,3])# (start, end, step by)
print(f)
print('reshape f into 8*3 matrix')
f=f.reshape([8,3])
print(f)
print('\n')

# linspace() fn
g=np.linspace(1,10,5)# (start, end , no of elements)
print("linspace",g)
print('\n')

# complex matrix
h=np.ones([5,4],dtype=complex)
print(h)
h=np.array([[1+2j,2+3j],[3+4j,4+5j]])
print(h)
print('\n')

# matrix dot product
x=np.array([[1,2,3],[3,4,5]])
y=np.array([[1,3],[4,5],[6,7]])
dt=np.dot(x,y)# dot() fn is used as dot product symbol @
print('matrix multiplication',dt)
print('\n')

# slicing in numpy
i=np.array([1,2,3,4,5,6,7,8,9,10])# slicing 1D matrix
print(i[2:4])
print(i[2:-1])
print(i[1:9:2])#[start:stop:step by]
i=np.array([[1,2,3],[3,4,5],[6,7,8],[9,0,1],[3,5,3]])# slicing 2D matrix
print(i)
print(i[:2,:-1])#  slice on basis of rows and cols
print(i[:,1])
print('\n')

# mathematical operations of matrix(numpy)
x=np.array([[1,2,3],[3,4,5]])
y=np.array([[1,3,4],[4,5,6]])
add=np.add(x,y)# addition
print(add)
sub=np.subtract(x,y)# substraction
print(sub)
div=np.divide(x,y)# division
print(div)
mul=np.multiply(x,y)# multiplication
print(mul)
sq=np.sqrt(x)# square root
print(sq)
ex=np.exp(y)#exponential
print(ex)
print(x+1)# matrix all elements increment by 1
print(y-1)# matrix all elements dicrement by 1
print(np.sin(x))# sin 
print(np.cos(y))# cos
print(np.tan(x))# tan
print('\n')

# special fn in numpy
i=np.array([1.2,2.7,3.3,4.6,5.5,6.5,7.1,8.9,9.4,10.2])
print(i)
m=np.round(i) # round fn() is used to round the figure
print(m)
m=np.floor(i) # floor fn() is used to round the figure to lower value
print(m)
m=np.ceil(i) # ceil fn() is used to round the figure to upper value
print(m)
print('\n')

# axis wise mathematical operations in numpy
x=np.array([[1,2,3],[3,4,5]])
print(x)
s=np.sum(x,axis=0)# col wise sum
print(s)
s=np.sum(x,axis=1)# row wise sum
print(s)
print('\n')

# array sort operation
j=np.array([5,8,4,6,7,3,2,0,1,9])
print(j)
srt=np.sort(j)
print(srt)
srt=np.sort(j)[::-1] # sort in reverse order
print(srt)
j=np.array([[1,5,3],[2,4,6]])# 2D matrix sort
print(j)
srt=np.sort(j)
print(srt)
srt=np.sort(j)[::-1] # sort in reverse order
print(srt)
srt=np.sort(j,axis=0) # axis wise sort sort col wise
print(srt)
srt=np.sort(j,axis=1) # axis wise sort sort row wise
print(srt)
srt=np.argsort(j) # display which index position changed
print(srt)
print('\n')

# min() & max() fn in numpy
j=np.array([5,8,4,6,7,3,2,0,1,9]) # 1d matrix
mx=np.max(j)
mn=np.min(j)
print(mx,mn)
amx=np.argmax(j) # return the index of the max value
amn=np.argmin(j) # return the index of the min value
print(amx,amn)
j=np.array([[1,5,3],[2,4,6]])# 2D matrix
print(j)
mx=np.max(j) # overall max number
print(mx)
mx=np.max(j,axis=1) # axis 1 refers to row
print(mx)
mx=np.max(j,axis=0)# axis 0 refers to col
print(mx)
mn=np.min(j,axis=1)
print(mn)
mn=np.min(j,axis=0)
print(mn)
print('\n')

# for loop in marix
j=np.array([5,8,4,6,7,3,2,0,1,9]) # 1d matrix
print('1D array')
for i in j :
    print(i)
m=np.array([[1,5,3],[2,4,6],[6,4,0]])# 2D matrix
print('2D matrix')
for i in m :
    for j in i :
       print(j)
m=np.array([[[1,2,3],[3,4,5],[6,7,8],[9,0,1],[3,5,3]]]) # 3D matrix
print('3D matrix')
for i in m :
    for j in i :
        for k in j:
            print(k)
print('\n')

# where(condition) fn return the index position of the value according to the data retrieved based on the condition
j=np.array([5,8,4,6,7,3,2,0,1,9]) # 1d matrix
d=np.where(j==4)
print(d)
d=np.where(j>5)
print(d)
# need to print the even number from the above matrix
j=np.sort(j)
evn=j[j%2==0] # first case
print(evn)
d=np.where(j%2==0) # second case
print(j[d])
print('\n')

# concatenate() fn in numpy
a=np.array([[1,5,3],[2,4,6],[6,4,0]])# 2D matrix
b=np.array([[1,2,3],[3,4,5],[6,7,8],[9,0,1],[3,5,3]])
m=np.concatenate((a,b))
print(m)
a.nbytes()# chech memory size of array

# cumulative sum
ars1=np.array([1,2,3,4])
print(ars1)
print(np.cumsum(ars1))

# clip values
ar1=np.array([1,5,10,15,20])
clipped=np.clip(ar1,5,15)
# it change the lower bound values to 5 
# upper bound values to 15
# 10 remain unchanged it is because 10 stace on the given range between 5 and 20
print(clipped)


#tile() fn in numpy library is used to repeat elements in that array
ars1=np.array([1,2,3,4,0])
ar1=np.array([1,5,10,15,20])
print(np.tile(ar1,3)) # repeat 3 times
print(np.repeat([1,5],4)) # repeat specified elements
print(np.dstack((ars1,ar1))) # it convert 2D into 3D 
print(np.meshgrid(ars1,ar1)) # meshgrid is used to create a coordinate grid from one-dimensional arrays
print(np.isnan(ar1))# check the elements is isNAN or not
print(np.nan_to_num(ar1)) # replace nan with zero
