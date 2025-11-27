import numpy as np
import matplotlib.pyplot as plt

x=np.arange(1,12,2)
y=np.arange(0,11,2)
plt.plot(x,y,marker='o',ms=10,mec='r',mfc='g')
# labeling x and y axis
plt.xlabel('x data') 
plt.ylabel('y data') 
# title of the graph
plt.title('data',loc='left')
# location of the title using loc
plt.show()