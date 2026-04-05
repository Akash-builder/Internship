import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("pizza_sales.csv")

# Convert date
df['order_date'] = pd.to_datetime(df['order_date'])

# ================= 1. DAILY TREND ================= #
daily_orders = df.groupby(df['order_date'].dt.date)['order_id'].nunique()

plt.figure()
daily_orders.plot(kind='bar')
plt.title("Daily Trend for Total Orders")
plt.xlabel("Date")
plt.ylabel("Orders")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../output/charts/daily_trend.png")

# ================= 2. MONTHLY TREND ================= #
monthly_orders = df.groupby(df['order_date'].dt.month)['order_id'].nunique()

plt.figure()
monthly_orders.plot(kind='line', marker='o')
plt.title("Monthly Trend for Orders")
plt.xlabel("Month")
plt.ylabel("Orders")
plt.tight_layout()
plt.savefig("../output/charts/monthly_trend.png")

# ================= 3. SALES BY CATEGORY ================= #
category_sales = df.groupby('pizza_category')['total_price'].sum()

plt.figure()
category_sales.plot(kind='pie', autopct='%1.1f%%')
plt.title("Sales by Pizza Category")
plt.ylabel("")
plt.savefig("../output/charts/category_sales.png")

# ================= 4. SALES BY SIZE ================= #
size_sales = df.groupby('pizza_size')['total_price'].sum()

plt.figure()
size_sales.plot(kind='pie', autopct='%1.1f%%')
plt.title("Sales by Pizza Size")
plt.ylabel("")
plt.savefig("../output/charts/size_sales.png")

# ================= 5. TOTAL PIZZAS BY CATEGORY ================= #
pizza_category_qty = df.groupby('pizza_category')['quantity'].sum()

plt.figure()
pizza_category_qty.plot(kind='bar')
plt.title("Total Pizzas Sold by Category")
plt.xlabel("Category")
plt.ylabel("Quantity")
plt.savefig("../output/charts/category_quantity.png")

# ================= 6. TOP 5 BEST SELLERS ================= #
top5 = df.groupby('pizza_name').agg({
    'total_price': 'sum',
    'quantity': 'sum',
    'order_id': 'nunique'
}).sort_values(by='total_price', ascending=False).head(5)

plt.figure()
top5['total_price'].plot(kind='bar')
plt.title("Top 5 Pizzas by Revenue")
plt.savefig("../output/charts/top5.png")

# ================= 7. BOTTOM 5 SELLERS ================= #
bottom5 = df.groupby('pizza_name').agg({
    'total_price': 'sum',
    'quantity': 'sum',
    'order_id': 'nunique'
}).sort_values(by='total_price').head(5)

plt.figure()
bottom5['total_price'].plot(kind='bar')
plt.title("Bottom 5 Pizzas by Revenue")
plt.savefig("../output/charts/bottom5.png")

