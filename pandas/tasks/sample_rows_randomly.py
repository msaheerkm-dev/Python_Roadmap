
import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({
    "id": range(1, 11),
    "value": list("abcdefghij")
})

print("Original DataFrame:")
print(df)

# Pick 3 random rows
print("\nRandom 3 rows:")
print(df.sample(n=3))

# Pick 30% random rows
print("\nRandom 30% rows:")
print(df.sample(frac=0.3))

print(df.sample(frac=.5))