import pandas as pd
import numpy as np
data = {
    "id": [1, 2, 3, 4, 5],
    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "email": [
        "alice@example.com", 
        "bob@example.com", 
        "charlie@example.com", 
        "bob@example.com",   # duplicate
        "alice@example.com"  # duplicate
    ]
}

df = pd.DataFrame(data)
print(df)
dupli=df.duplicated(subset='email',keep=False)
print(dupli)
df.drop_duplicates(subset=['email'],keep='first',inplace=True)
print(df)