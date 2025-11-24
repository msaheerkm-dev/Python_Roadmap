import pandas as pd

df = pd.DataFrame({
    'class': ['A','A','A','B','B','B','C','C','A'],
    'student': ['s1','s2','s3','s4','s5','s6','s7','s8','s9'],
    'score': [90, 85, 95, 70, 88, 92, 60, 75,83]
})
print(df)
top3=df.sort_values(['class','score'],ascending=[True,False])\
    .groupby('class').head(3)
top3['rank']=top3.groupby('class')['score'].rank(method='first',ascending=False)
print(top3)
top3['rank']=top3['rank'].replace({1.0:'first',2.0:'second',3.0:'third'})
print(top3)