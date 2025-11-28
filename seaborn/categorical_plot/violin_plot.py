import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# A violin plot is a combination of a boxplot + KDE (Kernel Density Estimate).
# it display the distribution more detail than boxplot
df=sns.load_dataset('iris')
sns.violinplot(x='species',y='sepal_length',data=df) 
plt.show()