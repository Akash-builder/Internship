import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
marks = [45,55,60,70,65,80,75,90,85,50,40,95,88,72,68]
df = pd.DataFrame({"Marks": marks})
print("Mean:", np.mean(marks))
print("Median:", np.median(marks))
print("Mode:", df["Marks"].mode()[0])
plt.hist(df["Marks"])
plt.title("Exam Marks Distribution")
plt.show()