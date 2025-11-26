#Given a DataFrame with missing values, replace all NaN in the Age column with the column’s mean.

import pandas as pd
import numpy as np

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, np.nan, 30, np.nan],
    "City": ["NY", "London", "Paris", "Berlin"]
}

df = pd.DataFrame(data)
print("Original:\n", df)
#df['Age']=df['Age'].replace(np.nan,df["Age"].agg("mean"))
df['Age'].fillna(df["Age"].mean(),inplace=True)
print(df)