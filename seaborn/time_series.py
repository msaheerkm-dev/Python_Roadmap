import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

flights = sns.load_dataset("flights")
flights["year"] = pd.to_datetime(flights["year"], format="%Y")
sns.lineplot(x="year", y="passengers", data=flights)
plt.show()
