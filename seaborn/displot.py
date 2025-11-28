import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# A displot (short for distribution plot) is a figure-level function 
# It is used to visualize the distribution of a variable.
# figure level
df=sns.load_dataset('tips')
sns.displot(df['total_bill'],kde=True)
plt.show()