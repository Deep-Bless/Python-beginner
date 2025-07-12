import pandas as pd
x=pd.read_csv("Sample_Sales_Data.csv")
print(x.duplicated().sum())
x=x.drop_duplicates()
print(x)