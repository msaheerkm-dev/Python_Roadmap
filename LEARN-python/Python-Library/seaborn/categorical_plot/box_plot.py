import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# it display mean , outsitter , quartiles
df=sns.load_dataset('iris')
sns.boxplot(x='species',y='sepal_length',data=df) 
# TO FIND OUT THE OUTSITTER FROM THE DATA
plt.show()

# boxenplot() Like a boxplot but better for large datasets with many observations.