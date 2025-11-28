import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# The histplot function is an axis-level plot used to show the distribution of a single variable
# or the relationship between two variables via a 2D histogram
df=sns.load_dataset('iris')
sns.histplot(x='species',data=df) 
plt.show()