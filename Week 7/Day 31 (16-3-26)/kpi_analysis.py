# Import required libraries
import pandas as pd

# Load dataset
df = pd.read_csv("pizza_sales.csv")

# Convert order_date to datetime
df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True, errors='coerce')
# ================= KPI CALCULATIONS ================= #

# 1. TOTAL REVENUE
total_revenue = df['total_price'].sum()

# 2. TOTAL ORDERS
total_orders = df['order_id'].nunique()

# 3. TOTAL PIZZAS SOLD
total_pizzas_sold = df['quantity'].sum()

# 4. AVERAGE ORDER VALUE
avg_order_value = total_revenue / total_orders

# 5. AVERAGE PIZZAS PER ORDER
avg_pizzas_per_order = total_pizzas_sold / total_orders

# ================= PRINT OUTPUT ================= #

print("------ KPI RESULTS ------")
print(f"Total Revenue: {total_revenue}")
print(f"Total Orders: {total_orders}")
print(f"Total Pizzas Sold: {total_pizzas_sold}")
print(f"Average Order Value: {avg_order_value:.2f}")
print(f"Average Pizzas per Order: {avg_pizzas_per_order:.2f}")

