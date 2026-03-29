import pandas as pd
s= pd.Series(['apple','banana','apple','orange'])

# convert to categorical
cat_s = s.astype('category')

#display category codes
print(cat_s.cat.codes)
