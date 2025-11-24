#Create a pivot table showing total sales per Region and Product.

import pandas as pd

data = {
    "Region": ["East", "East", "West", "West", "East", "West"],
    "Product": ["A", "B", "A", "B", "A", "B"],
    "Sales": [100, 200, 150, 250, 300, 400]
}

df = pd.DataFrame(data)

pvt=pd.pivot_table(df,values='Sales',columns='Product',index='Region',aggfunc=sum)
print(pvt)

