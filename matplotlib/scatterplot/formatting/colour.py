import numpy as np 
import matplotlib.pyplot as plt

x=np.random.randint(1,20,size=5)
y=np.random.randint(1,20,size=5)
cr=np.array(['red','green','blue','black','purple'])
plt.scatter(x,y,c=cr)
plt.show()