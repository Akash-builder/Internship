import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt   # ✅ REQUIRED

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

# Histplot
sns.histplot(data["Sales"], kde=True)
plt.show()

# Boxplot
sns.boxplot(x="Category", y="Sales", data=data)
plt.show()

# Barplot
sns.barplot(x="Region", y="Profit", data=data)
plt.show()

# Scatterplot
sns.scatterplot(x="Discount", y="Sales", data=data)
plt.show()

# Countplot
sns.countplot(x="Region", data=data)
plt.show()

# Jointplot (FIXED)
sns.jointplot(data)
plt.show()

# Pairplot
sns.pairplot(data)
plt.show()