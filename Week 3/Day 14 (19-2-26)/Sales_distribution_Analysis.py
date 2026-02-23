import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Sample salary data
salary = [25000, 30000, 32000, 28000, 35000, 40000, 45000, 50000,
52000, 55000, 60000, 62000, 65000, 70000, 72000,
80000, 90000, 120000, 150000, 300000]
df = pd.DataFrame({"Salary": salary})

Q1 = np.percentile(df["Salary"], 25)
Q2 = np.percentile(df["Salary"], 50) # Median
Q3 = np.percentile(df["Salary"], 75)
print("Q1:", Q1)
print("Median (Q2):", Q2)
print("Q3:", Q3)

print("BOXPLOT")
plt.boxplot(df["Salary"])
plt.title("Salary Distribution Boxplot")
plt.ylabel("Salary")
plt.show()