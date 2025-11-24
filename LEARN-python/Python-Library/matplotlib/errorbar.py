import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.arange(1,5)
y = np.random.randint(5,10,size=4)
errors = [0.5, 0.7, 0.3, 0.9]
plt.errorbar(x, y, yerr=errors, fmt='o r', capsize=5)
plt.show()
