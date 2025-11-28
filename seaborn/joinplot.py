import seaborn as sns
import matplotlib.pyplot as plt

# explore the relationship between two variables along with their individual distributions.
df=sns.load_dataset('tips')
sns.jointplot(data=df,x='total_bill',y='tip')
plt.show()
