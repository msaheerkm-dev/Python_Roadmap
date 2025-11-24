import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# A heatmap is a 2D representation of data where values are represented by colors.
# It’s often used to visualize:

# Correlation matrices

# Tabular data (like pivot tables)

# Confusion matrices in ML

df=sns.load_dataset('iris')
tc=df.corr(numeric_only=True)
sns.heatmap(tc,cmap='plasma',annot=True,linecolor='black')
plt.show()