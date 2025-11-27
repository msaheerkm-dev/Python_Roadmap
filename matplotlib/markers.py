import matplotlib.pyplot as plt
import numpy as np

x=np.arange(1,12,2)
y=np.arange(0,11,2)
plt.plot(x,y,'o',ms=10,mec='r',mfc='g') 
plt.show()
# marker='o' show points with line , ms represents marker size
# mec represents marker edge colour
# mfc represents marker face colour