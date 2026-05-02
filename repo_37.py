#4.2.3 City that Sold the Most Products
import pandas as pd

# Prompt the user for the file name
file_name = input()

# Load the data
df = pd.read_csv(file_name)

# write the code..
sale=df.groupby('City')['Quantity'].sum()
best_city=sale.idxmax()
# Display the result
print(f"City sold the most products: {best_city}")
