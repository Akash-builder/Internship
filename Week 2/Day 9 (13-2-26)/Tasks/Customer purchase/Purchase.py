import numpy as np 
data = np.array([ 
[101, 22, 1200, 1], 
[102, 25, 1800, 2], 
[103, 30, 1500, 1], 
[104, 28, 2200, 3], 
[105, 35, 900,  2], 
[106, 40, 2500, 3] 
]) 
# 1) Total customers 
total_customers = data.shape[0] 
# 2) Extract purchase column using slicing 
purchase_col = data[:, 2] 
# 3) Average purchase amount 
avg_purchase = np.mean(purchase_col) 
# 4) Maximum and minimum purchase 
max_purchase = np.max(purchase_col) 
min_purchase = np.min(purchase_col) 
# 5) Customers above average purchase 
above_avg_customers = data[purchase_col > avg_purchase] 
print("Dataset:\n", data) 
print("\n1) Total Customers:", total_customers) 
print("\n2) Purchase Column:\n", purchase_col) 
print("\n3) Average Purchase Amount:", avg_purchase) 
print("\n4) Maximum Purchase:", max_purchase) 
print("   Minimum Purchase:", min_purchase) 
print("\n5) Customers Above Average Purchase:\n", above_avg_customers)