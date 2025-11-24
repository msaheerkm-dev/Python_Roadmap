import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bob'],
    'skills': [['Python', 'SQL'], ['Java', 'C++', 'HTML']]
})

print("Original DataFrame:")
print(df)

# Exploding 'skills' column
exploded = df.explode('skills')

print("\nAfter explode:")
print(exploded)
