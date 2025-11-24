"""An outlier is a data point that is very different (too high or too low) compared to most other values.
Example: If most exam scores are between 40–90, but one student scored 0 or 1000, those are outliers.
"""
import pandas as pd


df = pd.DataFrame({"x": [10, 12, 14, 15, 16, 18, 20, 100]})
print("Original:\n", df)

q1 = df['x'].quantile(0.25)
q3 = df['x'].quantile(0.75)
iqr = q3 - q1
lo, hi = q1 - 1.5*iqr, q3 + 1.5*iqr

df['x_capped'] = df['x'].clip(lower=lo, upper=hi)
print("\nAfter Outlier Capping:\n", df)
