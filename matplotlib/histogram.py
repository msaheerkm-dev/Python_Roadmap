import numpy as np 
import matplotlib.pyplot as plt

x=np.random.normal(170,20,250)# (center , step , end)
plt.hist(x)
plt.show()