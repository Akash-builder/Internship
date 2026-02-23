import pandas as pd
import matplotlib.pyplot as plt
data = {
"Day": list(range(1,31)),
"Visitors": [200,220,210,250,270,260,300,310,305,320,
330,340,350,360,355,370,380,390,400,410,
420,430,440,450,460,470,480,490,500,520]

}
df = pd.DataFrame(data)
plt.plot(df["Day"], df["Visitors"])
plt.title("Website Traffic Trend")
plt.xlabel("Day")
plt.ylabel("Visitors")
plt.show()