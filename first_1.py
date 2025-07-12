import pandas as pd
data={

    'Name':['A1','A2','A3'],'Age':[23,34,27],'Experience':[2,3,4]
}
print(data)
x=pd.DataFrame(data)
print(x)
print("First row \n \n",x.head(1))
print("List of names \n ",x['Name'])
gender=['F','M','M']
x['Gender']=gender
print("After updates \n \n",x)
filter_df=x[x['Age']>25]
print("Age based fitering \n \n ",filter_df)
