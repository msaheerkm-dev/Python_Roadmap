import pandas as pd

df = pd.DataFrame({
    "class": ["A","A","B","B","C","C","A"],
    "subject": ["Math","Science","Math","Science","Math","Science","Math"],
    "score": [90, 85, 78, 82, 88, 92, 95]
})

print(df)
pivot = pd.pivot_table(df, 
                       values="score", 
                       index="class", 
                       columns="subject", 
                       aggfunc="mean")

print(pivot)
