import seaborn as sns
import matplotlib.pyplot as plt

# used in linear regression cases
df=sns.load_dataset('iris')
sns.lmplot(data=df,x='sepal_length',y='petal_length')
plt.show()
