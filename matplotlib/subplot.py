import matplotlib.pyplot as plt
import numpy as np
# plot 1
x=np.array([1,2,3,4])
y=np.array([3,6,1,10])
plt.subplot(2,3,1)
plt.title('plot 1')
plt.xlabel('X')
plt.ylabel('Y')
plt.plot(x,y)

#plot 2
x=np.array([1,2,3,4])
y=np.array([3,6,1,10])
plt.subplot(2,3,2)
plt.title('plot 2')
plt.xlabel('X')
plt.ylabel('Y')
plt.plot(x,y)

#plot 3
x=np.array([1,2,3,4])
y=np.array([3,6,1,10])
plt.subplot(2,3,3)
plt.title('plot 3')
plt.xlabel('X')
plt.ylabel('Y')
plt.plot(x,y)

#plot 4
x=np.array([1,2,3,4])
y=np.array([3,6,1,10])
plt.subplot(2,3,4)
plt.title('plot 4')
plt.xlabel('X')
plt.ylabel('Y')
plt.plot(x,y)

#plot 5
x=np.array([1,2,3,4])
y=np.array([3,6,1,10])
plt.subplot(2,3,5)
plt.title('plot 5')
plt.xlabel('X')
plt.ylabel('Y')
plt.plot(x,y)

#plot 6
x=np.array([1,2,3,4])
y=np.array([3,6,1,10])
plt.subplot(2,3,6)
plt.title('plot 6')
plt.xlabel('X')
plt.ylabel('Y')
plt.plot(x,y)

plt.suptitle('subplot')
plt.show()