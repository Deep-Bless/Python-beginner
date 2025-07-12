import pandas as pd

data_with_duplicates = {
    'Date': ['2024-01-01', '2024-01-02', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-04', '2024-01-05'],
    'Product': ['Widget A', 'Widget B', 'Widget B', 'Widget C', 'Widget D', 'Widget D', 'Widget E'],
    'Category': ['Electronics', 'Furniture', 'Furniture', 'Electronics', 'Clothing', 'Clothing', 'Electronics'],
    'Sales': [150, 200, 200, 340, 120, 120, 450],
    'Profit': [30, 50, 50, 80, 20, 20, 90]
}

df = pd.DataFrame(data_with_duplicates)
print(df.duplicated().sum())
df=df.drop_duplicates()
print(df)
