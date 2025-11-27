import numpy as np 
import matplotlib.pyplot as plt

# scatter 1
x=np.random.randint(1,20,size=10)
y=np.random.randint(1,20,size=10)
plt.scatter(x,y,c='red') # assign colour

# scatter 2
x1=np.random.randint(1,20,size=10)
y1=np.random.randint(1,20,size=10)
plt.scatter(x1,y1,c='green')

plt.show()