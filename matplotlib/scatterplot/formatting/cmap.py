import numpy as np 
import matplotlib.pyplot as plt

# colour map
x=np.random.randint(1,20,size=5)
y=np.random.randint(1,20,size=5)
plt.scatter(x,y,cmap='viridis')
plt.colorbar()
plt.show()