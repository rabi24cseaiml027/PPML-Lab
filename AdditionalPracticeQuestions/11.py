import pandas as pd
df1 = pd.DataFrame({
'ID':[1,2,3],
'Name':['Sushobhan','Ram','Syam']
})

df2 = pd.DataFrame({
'ID':[2,3,4],
'Age':[25,30,22]
})

merged_df = pd.merge(df1,df2,on='ID',how='right')
print(merged_df)
