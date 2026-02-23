import pandas as pd
import matplotlib.pyplot as plt
visitors = [1000,1200,1100,1500,1700]
conversions = [50,60,55,80,90]
conversion_rate = [(c/v)*100 for c,v in zip(conversions,visitors)]
plt.plot(conversion_rate)
plt.title("Website Conversion Rate")
plt.ylabel("Conversion %")
plt.show()