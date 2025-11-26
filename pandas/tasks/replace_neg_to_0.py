
import pandas as pd

df = pd.DataFrame({
    'A': [10, -5, 20, -15],
    'B': [5, -2, -8, 12],
    'C': [100, -50, 200, -300]
})

print("Original DataFrame:")
print(df)

# Subset of columns
cols = ['A', 'B','C']

# Clip values: set lower bound = 0
df[cols] = df[cols].clip(lower=0)

print("\nAfter replacing negatives in A & B using clip():")
print(df)