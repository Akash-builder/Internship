import pandas as pd
import matplotlib.pyplot as plt
cases = [10,15,20,30,45,60,90,130,200,300,
450,600,800,1000,1200]
df = pd.DataFrame({"Day":range(1,16),
"Cases":cases})
plt.plot(df["Day"], df["Cases"])
plt.title("COVID Cases Growth")
plt.show()