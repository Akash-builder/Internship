import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = {
"Day": list(range(1,31)),
"Price": [100,102,101,105,110,108,112,115,117,120,
118,119,122,125,123,128,130,135,133,137,
140,138,142,145,148,150,152,155,158,160]
}
df = pd.DataFrame(data)
print("Mean:", df["Price"].mean())
print("Std Dev:", df["Price"].std())
plt.plot(df["Day"], df["Price"])
plt.title("Stock Price Movement")
plt.xlabel("Day")
plt.ylabel("Price")
plt.show()