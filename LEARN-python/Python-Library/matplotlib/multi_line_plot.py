import matplotlib.pyplot as plt
import numpy as np

x1=np.random.randint(1,11,size=10)
y1=np.random.randint(1,11,size=10)
x2=np.random.randint(1,11,size=10)
y2=np.random.randint(1,11,size=10)

plt.plot(x1,y1,x2,y2)
plt.grid(True)
plt.show()