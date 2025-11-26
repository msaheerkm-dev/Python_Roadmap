import pandas as pd

data = {
    "Dept": ["HR", "HR", "IT", "IT", "Finance", "Finance"],
    "Gender": ["M", "F", "M", "M", "F", "F"]
}
df = pd.DataFrame(data)

# Crosstab: Count of employees by Dept and Gender
ct = pd.crosstab(df["Dept"], df["Gender"])
print(ct)
