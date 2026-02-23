import pandas as pd
import matplotlib.pyplot as plt
data = {"Status":["Active","Churned"],
"Count":[180,20]}
df = pd.DataFrame(data)
churn_rate = (20/200)*100
print("Churn Rate:", churn_rate,"%")
plt.pie(df["Count"], labels=df["Status"], autopct='%1.1f%%')
plt.title("Customer Churn Rate")
plt.show()