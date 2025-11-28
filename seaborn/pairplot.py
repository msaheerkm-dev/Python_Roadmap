import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# showing pairwise relationships between all numerical variables
df=sns.load_dataset('iris')
sns.pairplot(data=df,hue='species')
plt.show()