import pandas as pd
import matplotlib.pyplot as plt
data = {"Status":["Paid","Default"],
"Count":[90,10]}
df = pd.DataFrame(data)
default_rate = (10/100)*100
print("Default Rate:", default_rate,"%")
plt.bar(df["Status"], df["Count"])
plt.title("Loan Default Rate")
plt.show()