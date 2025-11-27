import numpy as np
import matplotlib.pyplot as plt

months=np.arange(1,13)
c1=np.arange(1,13)
c2=np.arange(12,24)
c3=np.arange(24,36)
plt.stackplot(months,c1,c2,c3,labels=['a','b','c'])
plt.legend()
plt.show()