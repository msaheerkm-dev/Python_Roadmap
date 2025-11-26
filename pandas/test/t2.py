#From the following DataFrame, fetch the top 3 salaries for each department.
#From the employee dataset, find the person(s) with the maximum salary in each department.
import pandas as pd
data = {
    "Dept": ["HR", "HR", "IT", "IT", "IT", "Finance", "Finance"],
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "George"],
    "Salary": [50000, 55000, 70000, 72000, 71000, 60000, 62000]
}

df = pd.DataFrame(data)
df=df.groupby('Dept').apply(lambda x: x.nlargest(3,'Salary')).reset_index(drop=True)
# find person with highest salary in each department 
df=df.sort_values(['Salary'],ascending=False).groupby('Dept').head(1)
print(df)