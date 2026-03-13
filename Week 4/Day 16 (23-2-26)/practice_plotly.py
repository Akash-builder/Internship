import plotly.express as px
import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)

# Create synthetic data
n = 300

data = pd.DataFrame({
    "Date": pd.date_range(start="2024-01-01", periods=n, freq="D"),
    "Region": np.random.choice(["North", "South", "East", "West"], n),
    "Category": np.random.choice(["Electronics", "Clothing", "Home", "Sports"], n),
    "Sales": np.random.normal(500, 120, n).round(2),
    "Profit": np.random.normal(80, 30, n).round(2),
    "Quantity": np.random.randint(1, 20, n),
    "Discount": np.random.uniform(0, 0.3, n).round(2),
    "Customer_Age": np.random.randint(18, 65, n)
})

#Ploty Graph
d1=px.bar(data,x="Category",y="Sales",color="Region")
d1.show()
