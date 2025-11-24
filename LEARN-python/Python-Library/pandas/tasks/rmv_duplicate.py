import pandas as pd

df = pd.DataFrame({
    "id": [1, 2, 2, 3, 3, 3],
    "name": ["A", "B", "B", "C", "C", "C"]
})

print("Original:")
print(df)

# Remove duplicates, keep first
print("\nKeep first:")
print(df.drop_duplicates(keep="first"))

# Remove duplicates, keep last
print("\nKeep last:")
print(df.drop_duplicates(keep="last"))

# Remove all duplicates (keep none)
print("\nDrop all duplicates:")
print(df.drop_duplicates(keep=False))
