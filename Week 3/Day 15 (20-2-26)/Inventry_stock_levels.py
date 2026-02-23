import matplotlib.pyplot as plt
stock = [500,480,460,450,430,400,380,360,340,300]
plt.plot(stock)
plt.axhline(y=350, color='r')
plt.title("Inventory Stock Levels")
plt.show()