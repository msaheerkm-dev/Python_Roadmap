import numpy as np 
import matplotlib.pyplot as plt

x=np.random.randint(1,20,size=5)
y=np.random.randint(1,20,size=5)
sz=np.array([10,25,50,10,17])
plt.scatter(x,y,s=sz)
plt.show()