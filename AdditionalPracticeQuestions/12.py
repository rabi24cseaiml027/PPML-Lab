import pandas as pd
import matplotlib.pyplot as plt

# Create a sample DataFrame
df = pd.DataFrame({
    'Year': [2017, 2018, 2019, 2020, 2021],
    'Sales': [200, 250, 300, 350, 400]
})

# Plot the 'Year' against 'Sales' using a line plot
plt.plot(df['Year'], df['Sales'])

# Add labels and a title
plt.xlabel('Year')
plt.ylabel('Sales')
plt.title('Yearly Sales Trend')

# Display the plot
plt.show()
