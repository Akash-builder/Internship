import pandas as pd
import numpy as np
# Create Sample Data
data = {
"Customer ID": ["C101","C102","C103","C101"],
"Order ID": [1001,1002,1003,1001],
"Gender": ["m","f","M","m"],
"Age": [25,-5,200,25],
"City": ["New York","Chicago",None,"New York"],
"Product Name": ["Laptop","T-shirt","AC","Laptop"],
"Product Category":
["electronics","Fashion","APPLIANCES","electronics"],
"Quantity": [1,2,1,1],
"Price": [60000,700,65000,60000],
"Order Date": ["2025-01-02","2025-01-03","2025-01-06","2025-01-02"]
}
df = pd.DataFrame(data)

df = df.drop_duplicates(subset="Order ID")

df["Gender"] = df["Gender"].str.lower()
df["Gender"] = df["Gender"].replace({"m":"male","f":"female"})

df.loc[(df["Age"] < 0) | (df["Age"] > 100), "Age"] = np.nan
df["Age"].fillna(df["Age"].median(), inplace=True)

df["City"].fillna(df["City"].mode()[0], inplace=True)

df["Product Category"] = df["Product Category"].str.lower()

df["Order Date"] = pd.to_datetime(df["Order Date"])

df["Month"] = df["Order Date"].dt.month_name()

df["Day"] = df["Order Date"].dt.day_name()

df.columns = df.columns.str.lower()

df["total_revenue"] = df["quantity"] * df["price"]
total_revenue = df["total_revenue"].sum()
print("Total Revenue:", total_revenue)

top_cities =df.groupby("city")["total_revenue"].sum().sort_values(ascending=False)
print(top_cities)

category_sales = df.groupby("product category")["total_revenue"].sum()
print(category_sales)