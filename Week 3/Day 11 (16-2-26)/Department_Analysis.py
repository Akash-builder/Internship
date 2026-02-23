import pandas as pd
# Create sample dataset
data = {
"Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace"],
"Dept": ["HR", "IT", "IT", "Finance", "HR", "Finance", "IT"],
"Salary": [40000, 60000, 65000, 55000, 42000, 58000, 70000]
}
df = pd.DataFrame(data)
print("Employee DataFrame:")
print(df)
it_employees = df[df["Dept"] == "IT"]

print("\nFiltered IT Department:")
print(it_employees)
grouped = df.groupby("Dept").agg(
Total_Salary=("Salary", "sum"),
Average_Salary=("Salary", "mean"),
Employee_Count=("Salary", "count")
)
print("\nGrouped by Department:")
print(grouped)