import pandas as pd
import numpy as np

df=pd.DataFrame({
    "values":range(1,11),
    "alpha":list("abcdefghij")
})
print(df)
#df.loc[[1,3,5],'values']=np.nan
df['values']=df['values'].replace([1,3,5],np.nan)
print(df.isna())# to detect
print(df.isna().sum())# to count
print(df.fillna(0))# to fill value

