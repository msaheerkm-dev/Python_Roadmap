import pandas as pd

df = pd.DataFrame({
    "age": [25, "30", "??", "forty", 50, "60"],
    "name": ["a","b","c","d","e","f"]
})

# Try converting to numeric; non-numeric → NaN
bad_rows = df[pd.to_numeric(df["age"], errors="coerce").isna()]


print(bad_rows)
