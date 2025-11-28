import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# A line plot is used to show the relationship between two continuous variables
df=sns.load_dataset('iris')
print(df)
sns.lineplot(x='sepal_length',y='sepal_width',data=df)
plt.title(' flower data set')
plt.show()
