import pandas as pd

s = pd.Series(['1,000', '2,500', '3,750'])

# Remove commas and convert to float
float_s = s.str.replace(',', '').astype(float)#after removing the commas converts strings to float type

print(float_s)
