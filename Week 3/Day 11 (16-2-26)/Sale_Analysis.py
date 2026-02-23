import pandas as pd

# Sample product dataset
data = {
"Product_ID": [101,102,103,104,105,106,107,108],
"Product_Name": ["Laptop","Mobile","Tablet","Headphones",
"Monitor","Keyboard","Mouse","Printer"],
"Quantity": [10,25,15,40,8,50,60,5],
"Price": [60000,20000,30000,2000,15000,1000,500,12000]
}
df = pd.DataFrame(data)
print("Product Data:")
print(df)
df["Total_Price"] = df["Quantity"] * df["Price"]
print("\nData with Total Price:")
print(df)
top5 = df.sort_values(by="Total_Price", ascending=False).head(5)
print("\nTop 5 Products Based on Total Price:")
print(top5)