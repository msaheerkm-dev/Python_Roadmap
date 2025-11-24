import numpy as np 
import matplotlib.pyplot as plt

x=np.array(['A','B','C','D','E'])
y=np.array([10,16,25,14,10])
plt.barh(x,y,color='red')# default bar() is vertical
plt.show()