import pandas as pd

df = pd.DataFrame({
    "date": pd.date_range("2025-01-01", periods=6),
    "value": [10, None, None, 25, None, 40]
}).set_index("date")

print("Original:")
print(df)

# Forward Fill
df_ffill = df.fillna(method="ffill")
print("\nForward Fill (ffill):")
print(df_ffill)#Each missing value is replaced with the last known value

# Backward fill
df_bfill = df.fillna(method="bfill")
print("\nBackward Fill (bfill):")
print(df_bfill)# Each missing value is replaced with the next known value.