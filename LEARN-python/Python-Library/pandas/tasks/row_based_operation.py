import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'first_name': ['John', 'Jane', 'Sam', 'Anna'],
    'last_name': ['Doe', 'Smith', 'Brown', 'Taylor']
})

print("Original DataFrame:")
print(df)

# Row-wise operation: join first_name and last_name
df['full name']=df[['first_name','last_name']].agg(" ".join,axis=1)
print(df)