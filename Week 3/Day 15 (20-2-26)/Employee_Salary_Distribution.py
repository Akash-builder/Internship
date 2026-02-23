import pandas as pd
import matplotlib.pyplot as plt
salaries = [25000,30000,32000,28000,35000,40000,42000,45000,
47000,50000,52000,55000,60000,65000,70000]
df = pd.DataFrame({"Salary": salaries})
print("Q1:", df["Salary"].quantile(0.25))
print("Median:", df["Salary"].median())
print("Q3:", df["Salary"].quantile(0.75))
plt.boxplot(df["Salary"])
plt.title("Salary Distribution")
plt.show()