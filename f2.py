import pandas as pd
data={

    'Name':['A1','A2','A3'],'Age':[23,34,27],'Experience':[2,3,4]
}
print(data)
x=pd.DataFrame(data)

gender=['F','M','M']
x['Gender']=gender
print(x)
Sorted_data=x.sort_values(by='Age',ascending=False)
print("After sorting \n ",Sorted_data)
Age_mean=x.groupby('Gender')['Age'].mean()
print("Mean wise Age ",Age_mean)