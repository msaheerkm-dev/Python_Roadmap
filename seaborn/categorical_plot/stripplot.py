import seaborn as sns
import matplotlib.pyplot as plt

# Instead of summarizing (like boxplot or violinplot), it shows each data point, which helps you see:

# Data spread

# Outliers

# Number of data points
df=sns.load_dataset('iris')
sns.stripplot(x='species',y='sepal_length',data=df,jitter=True,hue='petal_width')
plt.show()

# swarmplot() is like stripplot, but avoid overlapping 