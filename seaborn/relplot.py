import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np

# used to visualize relationships between variables
tips = sns.load_dataset("tips")
sns.relplot(x="total_bill", y="tip", hue="smoker", data=tips, kind="line")
plt.show()
