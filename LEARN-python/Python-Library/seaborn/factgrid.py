import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

tips=sns.load_dataset('tips')
g = sns.FacetGrid(tips, col="sex", row="smoker")
g.map(sns.scatterplot, "total_bill", "tip")
plt.show()
