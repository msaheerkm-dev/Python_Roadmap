import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# display the points of rerlation not line
df=sns.load_dataset('car_crashes')
plt.scatter(df.speeding,df.alcohol)
plt.show()
