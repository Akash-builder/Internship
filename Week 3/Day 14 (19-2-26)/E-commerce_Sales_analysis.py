import numpy as np
import pandas as pd
from scipy import stats
# Create sample sales data for 30 days
sales = [50000, 52000, 48000, 51000, 53000, 47000, 55000, 60000, 62000,
58000,
54000, 56000, 59000, 61000, 63000, 65000, 64000, 66000, 67000,
69000,
70000, 72000, 71000, 73000, 74000, 76000, 75000, 77000, 78000,
80000]
days = np.arange(1, 31)
df = pd.DataFrame({
"Day": days,
"Sales": sales
})
df.head()

print("MEAN MEDIAN MODE")
mean_sales = np.mean(df["Sales"])
median_sales = np.median(df["Sales"])
mode_sales = stats.mode(df["Sales"], keepdims=True)
print("Mean:", mean_sales)
print("Median:", median_sales)
print("Mode:", mode_sales.mode[0])

print("STANDERD DEVIATION AND VARIANCE")
std_sales = np.std(df["Sales"])
var_sales = np.var(df["Sales"])
print("Standard Deviation:", std_sales)
print("Variance:", var_sales)

print("CORRELATION")
correlation = np.corrcoef(df["Day"], df["Sales"])[0,1]
print("Correlation between Day & Sales:", correlation)