import numpy as np 
import plotly.graph_objects as go 
from plotly.subplots import make_subplots 
np.random.seed(100) 
# ----------------------------- 
# Synthetic Retail Data 
# ----------------------------- 
days = np.arange(1, 121) 
revenue = np.cumsum(np.random.randint(200, 500, 120)) 
cost = np.cumsum(np.random.randint(100, 300, 120)) 
profit = revenue - cost 
orders = np.random.randint(30, 150, 120) 
# Category Sales 
category_labels = ["Electronics", "Clothing", "Home Decor", "Sports"] 
category_sales = [35, 25, 20, 20] 
# Region Sales 
region_labels = ["North", "South", "East", "West"] 
region_sales = [30, 25, 25, 20] 
# ----------------------------- 
# Create Subplot Layout 
# ----------------------------- 
fig = make_subplots( 
rows=3, cols=2, 
specs=[ 
[{"colspan": 2}, None], 
[{"type": "scatter"}, {"type": "bar"}], 
[{"type": "pie"}, {"type": "indicator"}] 
], 
subplot_titles=( 
"Revenue & Profit Trend", 
"Order Growth", 
"Monthly Revenue", 
"Category Distribution", 
"Revenue KPI" 
) 
) 
# ----------------------------- 
# Revenue & Profit Trend 
# ----------------------------- 
fig.add_trace( 
go.Scatter(x=days, y=revenue, mode="lines", name="Revenue"), 
row=1, col=1 
) 
fig.add_trace( 
go.Scatter(x=days, y=profit, mode="lines", name="Profit"), 
row=1, col=1 
) 
# ----------------------------- 
# Order Growth Scatter 
# ----------------------------- 
fig.add_trace( 
go.Scatter(x=days, y=orders, mode="markers", name="Orders"), 
row=2, col=1 
) 
# ----------------------------- 
# Monthly Aggregation (6 Months) 
# ----------------------------- 
monthly_rev = np.array_split(revenue, 6) 
monthly_sum = [m.sum() for m in monthly_rev] 
fig.add_trace( 
go.Bar( 
x=["M1","M2","M3","M4","M5","M6"], 
y=monthly_sum, 
name="Monthly Revenue" 
), 
row=2, col=2 
) 
# ----------------------------- 
# Category Pie Chart 
# ----------------------------- 
fig.add_trace( 
go.Pie( 
labels=category_labels, 
values=category_sales, 
hole=0.4 
), 
row=3, col=1 
) 
# ----------------------------- 
# KPI Indicator 
# ----------------------------- 
target = 50000 
fig.add_trace( 
go.Indicator( 
mode="gauge+number+delta", 
value=np.sum(revenue), 
delta={'reference': target}, 
gauge={ 
'axis': {'range': [0, 100000]}, 
}, 
title={'text': "Total Revenue vs Target"} 
), 
row=3, col=2 
) 
# ----------------------------- 
# Dropdown Filter 
# ----------------------------- 
fig.update_layout( 
updatemenus=[ 
dict( 
buttons=[ 
dict(label="Show All", 
method="update", 
args=[{"visible": [True]*6}]), 
dict(label="Only Revenue", 
method="update", 
args=[{"visible": [True, False, False, False, False, 
False]}]), 
dict(label="Only Orders", 
method="update", 
args=[{"visible": [False, False, True, False, False, 
False]}]) 
], 
direction="down", 
showactive=True, 
x=0.1, 
y=1.15 
) 
] 
) 
# ----------------------------- 
# Range Slider for Trend 
# ----------------------------- 
fig.update_xaxes( 
rangeslider_visible=True, 
row=1, col=1 
) 
# ----------------------------- 
# Layout 
# ----------------------------- 
fig.update_layout( 
height=900, 
width=900, 
title="Retail Business Intelligence Dashboard", 
template="plotly_dark" 
) 
fig.show()