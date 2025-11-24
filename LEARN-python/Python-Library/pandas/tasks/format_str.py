import pandas as pd

df = pd.DataFrame({
    "city": ["  new york ", "LOS  ANGELES", " san   francisco", None, "   BOSTON  "]
})

df['city'] = (df['city'].astype(str)      # make sure it's string
                 .str.strip()             # remove leading/trailing spaces
                 .str.title()             # capitalize first letter of each word
                 .str.replace(r'\s+', ' ', regex=True))  # replace multiple spaces with single space


print(df)
