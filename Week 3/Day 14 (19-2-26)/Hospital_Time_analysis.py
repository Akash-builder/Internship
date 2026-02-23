import numpy as np
import pandas as pd
from scipy.stats import skew
import matplotlib.pyplot as plt
# Sample waiting time data (in minutes)
waiting_time = [5, 10, 7, 12, 8, 6, 9, 15, 20, 25,
30, 18, 7, 6, 5, 8, 9, 10, 45, 60]
df = pd.DataFrame({"Waiting_Time": waiting_time})

print("VARIANCE AND RANGE")
variance = np.var(df["Waiting_Time"])
range_value = np.max(df["Waiting_Time"]) - np.min(df["Waiting_Time"])
print("Variance:", variance)
print("Range:", range_value)

print("IDENTIFY SKEWNESS")
skewness_value = skew(df["Waiting_Time"])
print("Skewness:", skewness_value)

print("DETECT OUTLIERS USING IQR")
Q1 = np.percentile(df["Waiting_Time"], 25)
Q3 = np.percentile(df["Waiting_Time"], 75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = df[(df["Waiting_Time"] < lower_bound) |
(df["Waiting_Time"] > upper_bound)]
print("Outliers:")
print(outliers)

print("BOXPLOT")
plt.boxplot(df["Waiting_Time"])
plt.title("Hospital Waiting Time Boxplot")
plt.ylabel("Waiting Time (Minutes)")
plt.show()