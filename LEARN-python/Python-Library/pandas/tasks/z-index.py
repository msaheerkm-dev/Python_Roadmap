# z index using transform
import pandas as pd


data = {
    'class': ['A','A','A','B','B','B'],
    'marks': [80, 90, 75, 60, 70, 85]
}

df = pd.DataFrame(data)
df['zscore']=df.groupby('class')['marks'].transform(lambda x: (x - x.mean()) / x.std())
print(df)