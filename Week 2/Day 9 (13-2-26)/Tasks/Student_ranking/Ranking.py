import pandas as pd 
import numpy as np 
# Sample student dataset 
data = { 
"Name": ["Akash", "Ravi", "Priya", "Anjali", "Kiran", "Sneha"], 
"Department": ["CSE", "ECE", "CSE", "ISE", "ME", "EEE"], 
"Marks": [88, 76, 92, 85, 70, 95] 
} 
df = pd.DataFrame(data) 
# Sorting students by marks (Descending) 
df_sorted = df.sort_values(by="Marks", ascending=False) 
# Assign rank 
df_sorted["Rank"] = np.arange(1, len(df_sorted) + 1) 
# Top 3 students 
top3 = df_sorted.head(3) 
print("Student Ranking List:\n", df_sorted) 
print("\nTop 3 Students:\n", top3)