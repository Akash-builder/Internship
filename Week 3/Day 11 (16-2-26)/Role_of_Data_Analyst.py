#step 1 loading datd & prepare
import pandas as pd
df = pd.read_excel("ecommerce.xlsx")
# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])
# Create Total Revenue column
df["total_revenue"] = df["quantity"] * df["price"]
df.head()

total_revenue = df["total_revenue"].sum()
print("Total Revenue:", total_revenue)

#step 2 Total Revenue
total_revenue = df["total_revenue"].sum()
print("Total Revenue:", total_revenue)

#step 3 Top 5 Products
top_products = (
df.groupby("product_name")["total_revenue"]
.sum()
.sort_values(ascending=False)
.head(5)
)
print(top_products)

#step 4 Daily Trends
daily_trend = df.groupby("date")["total_revenue"].sum()
print(daily_trend)

#step 5 Monthly Sales
df["month"] = df["date"].dt.to_period("M")
monthly_sales = df.groupby("month")["total_revenue"].sum()
print(monthly_sales)

#step 6 Customer Segementation
customer_spend = df.groupby("customer_id")["total_revenue"].sum()
segmentation = pd.cut(
customer_spend,
bins=[0, 50000, 200000, float("inf")],
labels=["Low Value", "Medium Value", "High Value"]
)
customer_segment = pd.DataFrame({
"Total_Spend": customer_spend,
"Segment": segmentation
})
print(customer_segment)

#step 7 High Valued Customers
high_value_customers = customer_spend[customer_spend > 200000]
print(high_value_customers)

#step 8 Regional Performance
regional_performance = (
df.groupby("region")["total_revenue"]
.sum()
.sort_values(ascending=False)

)
print(regional_performance)