import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# So instead of just counting (like countplot), it aggregates numerical values and then plots bars.
df=sns.load_dataset('iris')
sns.barplot(x='species',y='sepal_length',data=df,palette='coolwarm')
plt.show()
