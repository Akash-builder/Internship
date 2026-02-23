import pandas as pd
import matplotlib.pyplot as plt
orders = [50,60,55,70,80,75,90,100,95,110,
120,130,125,140,150,145,160,170,165,180,
190,200,195,210,220,215,230,240,235,250]
revenue = [o*100 for o in orders]
df = pd.DataFrame({"Orders":orders,
"Revenue":revenue})
print("Correlation:", df["Orders"].corr(df["Revenue"]))
plt.plot(orders)
plt.title("Daily Orders")
plt.show()