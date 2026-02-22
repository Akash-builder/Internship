import pandas as pd
import numpy as np 
# Sample production dataset 
data = { 
"ProductID": ["P101","P102","P103","P104","P105","P106","P107"], 
"Defects": [0, 2, 5, 1, 4, 0, 6] 
} 
df = pd.DataFrame(data) 
# Add status column using NumPy 
df["Status"] = np.where(df["Defects"] > 3, "Defective", "Pass") 
# 1) Total Pass and Defective count 
status_count = df["Status"].value_counts() 
# 2) Defect rate (%) 
defect_rate = (status_count.get("Defective", 0) / len(df)) * 100 
# 3) High defect products (defects > 3) 
high_defect_products = df[df["Defects"] > 3] 
print("Production Quality Dataset:\n", df) 
print("\nPass vs Defective Count:\n", status_count) 
print("\nDefect Rate (%):", defect_rate) 
print("\nHigh Defect Products:\n", high_defect_products)