import scipy.stats as stats
import matplotlib.pyplot as plt

data=[0,1,2,1,2,3,4,5,2,4]
stats.probplot(data,plot=plt)# probablity plot
plt.show()

