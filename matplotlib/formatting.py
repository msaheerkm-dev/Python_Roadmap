import numpy as np
import matplotlib.pyplot as plt

x=np.random.randint(1,11,size=10)
plt.plot(x,'o:r')
# 'o' represents the marker 
# ':' represemts the dotted line 
# 'r' represents the red colour
# linestyle='dotted 
# c='r' here c represents the line colour 
plt.show()