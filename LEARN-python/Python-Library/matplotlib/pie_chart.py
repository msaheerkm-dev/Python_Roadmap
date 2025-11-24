import numpy as np
import matplotlib.pyplot as plt

x=np.array([20,25,25,30])
lb=np.array(['A','B','C','D'])
exp=np.array([0.2,0,0,0])
plt.pie(x,labels=lb,explode=exp,shadow=True) # explode used to seperate a single data
plt.legend()
plt.show()