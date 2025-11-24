
#Given daily stock prices, compute a 3-day rolling average.

import pandas as pd

data = {
    "Day": [1, 2, 3, 4, 5, 6],
    "Price": [10, 20, 30, 40, 50, 60]
}

df = pd.DataFrame(data)
print(df)
df['rolling']=df['Price'].rolling(window=2).mean()
print(df)