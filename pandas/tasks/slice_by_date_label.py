import pandas as pd

rng=pd.date_range("2025-01-01", periods=10)
df=pd.DataFrame({'value':range(1,11)},index=rng)
print(df)
df=df.loc["2025-01-04":"2025-01-08"]
print(df)