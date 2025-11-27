import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure()
ax=plt.axes(projection='3d')
x = [1,2,3,4,5]
y = [5,6,2,3,13]
z = [2,3,3,3,5]
ax.scatter(x,y,z)
plt.show()