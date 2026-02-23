import pandas as pd
import matplotlib.pyplot as plt
temps = [30,32,31,29,28,35,36,34,33,37,
38,39,40,41,42,38,37,36,35,34,
33,32,31,30,29,28,27,26,25,24]
df = pd.DataFrame({"Day":range(1,31),
"Temperature":temps})
print("Range:", max(temps)-min(temps))
plt.plot(df["Day"], df["Temperature"])
plt.title("Temperature Variation")
plt.show()