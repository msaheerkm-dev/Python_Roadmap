import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# A count plot is used to show the frequency (count) of categories in a categorical variable.
df=sns.load_dataset('iris')
sns.countplot(x='species',data=df)
sns.boxplot()
plt.show()
