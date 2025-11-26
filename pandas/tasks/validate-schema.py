"""import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    "name": Column(str),
    "age": Column(int),
    "salary": Column(float)
})

schema.validate(df)  # raises error if schema is wrong"""

"""expected_schema = {
    "name": "object",
    "age": "int64",
    "salary": "float64"
}

for col, dtype in expected_schema.items():
    if col not in df.columns:
        print(f"❌ Missing column: {col}")
    elif df[col].dtype != dtype:
        print(f"❌ Column {col} has dtype {df[col].dtype}, expected {dtype}")
    else:
        print(f"✅ {col} OK")"""

