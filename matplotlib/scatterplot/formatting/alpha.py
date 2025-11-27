import numpy as np 
import matplotlib.pyplot as plt

# alpha transparency
x=np.random.randint(1,20,size=5)
y=np.random.randint(1,20,size=5)
af=np.array([0,0.3,0.6,0.9,1])
plt.scatter(x,y,alpha=af) # transparency of the scatter plot
plt.show()