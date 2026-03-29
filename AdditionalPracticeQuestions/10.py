import pandas as pd

# Simple sales dataset
data = {
    'customer_id': [101, 102, 101, 103, 102, 101],
    'salesman_id': [1, 2, 1, 3, 2, 2],
    'amount': [500, 300, 200, 400, 150, 250]
	}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
# Group by customer_id and salesman_id and count rows
result = df.groupby(['customer_id', 'salesman_id']).size().reset_index(name='count')
#Group → Count rows → Convert to table(INTO A PROPERDATAFRAME)
print("\nGrouped Count:")
print(result)
