import matplotlib.pyplot as plt
forecast = [200,220,250,270,300]
actual = [210,215,260,280,290]
plt.plot(forecast, label="Forecast")
plt.plot(actual, label="Actual")
plt.legend()
plt.title("Forecast vs Actual Sales")
plt.show()