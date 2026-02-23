import pandas as pd
# Customer Details
customers = pd.DataFrame({
"customer_id": [1, 2, 3, 4, 5],
"customer_name": ["Alice", "Bob", "Charlie", "David", "Eva"],
"city": ["New York", "Chicago", "Los Angeles", "Houston", "Phoenix"]
})
print("Customer Dataset:")
print(customers)
import pandas as pd
# Order Details
orders = pd.DataFrame({
"order_id": [101, 102, 103, 104, 105, 106],
"customer_id": [1, 2, 1, 3, 4, 2],
"product": ["Laptop", "Mobile", "Tablet", "Monitor", "Keyboard",
"Mouse"],
"amount": [60000, 20000, 30000, 15000, 1000, 500]
})
print("\nOrder Dataset:")
print(orders)
merged_data = pd.merge(customers, orders, on="customer_id", how="inner")
print("\nMerged Dataset:")
print(merged_data)