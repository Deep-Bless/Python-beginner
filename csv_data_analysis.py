import matplotlib.pyplot as plt
import pandas as pd
x=pd.read_csv("Sample_Sales_Data.csv")
x['Category']=x['Category'].str.lower()
print(x.head(2).to_string(index=False))

print(x.describe().to_string(index=False))
#missing value
print(x.isnull().sum())
data_date=pd.to_datetime(x['Date'])
print(data_date)
cate_wise = x.groupby("Category").agg({'Sales': 'sum', 'Profit': 'sum'})
print(cate_wise)
higher_profit=x[x['Profit']>60]
print(higher_profit)