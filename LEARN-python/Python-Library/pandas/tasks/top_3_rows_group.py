import pandas as pd

df = pd.DataFrame({
    'class': ['A','A','A','B','B','B','C','C','A'],
    'student': ['s1','s2','s3','s4','s5','s6','s7','s8','s9'],
    'score': [90, 85, 95, 70, 88, 92, 60, 75,83]
})

print(df)
# using head()
top3=df.sort_values(['class','score'],ascending=[True,False])\
    .groupby('class').head(3)
print(top3)

'''using nlargest
top3=df.groupby('class').apply(lambda x:x.nlargest(3,'score'))\
    .reset_index(drop=True)'''

"""using rank
top3=df[df.groupby('class')['score']\
    .rank(method='first',ascending=False)<=2]
"""
