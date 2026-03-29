'''
write a pandas program to ceate a dataframe from dictionary
where values are lists of unequal lengths by filling missing values with None.'''

import pandas as pd
data = {
	'A':[1,2,3],
	'B':[4,5],
	'C':[6,7,8,9]
	}

df = pd.DataFrame(dict([(k,pd.Series(v)) for k,v in data.items()]))

df = df.where(pd.notnull(df),None)

print(df)

