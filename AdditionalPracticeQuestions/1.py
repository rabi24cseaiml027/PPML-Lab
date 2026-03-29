import pandas as pd

s = pd.Series(['10', '20', 'abc', '30'])

# Convert to numeric, invalid parsing will be set as NaN
numeric_s = pd.to_numeric(s, errors='coerce')#

print(numeric_s)
