import seaborn as sns 
import matplotlib.pyplot as plt

# sns.catplot() is a figure-level function for categorical plots (bar, box, strip, etc.).
tips=sns.load_dataset('tips')
sns.catplot(x="day", y="total_bill", kind="strip", data=tips)
plt.show()
