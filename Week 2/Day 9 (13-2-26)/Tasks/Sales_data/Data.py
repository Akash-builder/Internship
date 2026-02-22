import pandas as pd 
import numpy as np 
# Sample dataset 
data = { 
"Month": 
["Jan","Jan","Jan","Feb","Feb","Feb","Mar","Mar","Mar","Apr","Apr","Apr"], 
"Region": ["North","South","West","North","South","West","North","South","West","North","South","West"], 
"Sales":  [12000, 15000, 11000, 13500, 16000, 12500, 14000, 17000, 13000, 15500, 18000, 14500] 
} 
df = pd.DataFrame(data) 
# 1) Total sales per region 
total_sales_per_region = df.groupby("Region")["Sales"].sum() 
# 2) Average sales per month 
avg_sales_per_month = df.groupby("Month")["Sales"].mean() 
# 3) Best performing region 
best_region = total_sales_per_region.idxmax() 
print("Total Sales per Region:\n", total_sales_per_region) 
print("\nAverage Sales per Month:\n", avg_sales_per_month) 
print("\nBest Performing Region:", best_region)