import numpy as np 
import plotly.graph_objects as go 
from plotly.subplots import make_subplots 
np.random.seed(202) 
# ----------------------------- 
# Synthetic Uber Data 
# ----------------------------- 
days = np.arange(1, 121) 
rides = np.random.randint(200, 600, 120) 
fare_per_ride = np.random.uniform(8, 25, 120) 
surge_multiplier = np.random.uniform(1, 2, 120) 
revenue = rides * fare_per_ride * surge_multiplier 
distance = np.random.uniform(2, 20, 120) 
# Ride Type Distribution 
ride_types = ["UberX", "UberXL", "Uber Black", "Uber Pool"] 
ride_type_share = [50, 20, 15, 15] 
# City Zone Distribution 
zones = ["North", "South", "East", "West"] 
zone_share = [30, 25, 25, 20] 
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
"Ride Demand & Revenue Trend", 
"Ride Distance Pattern", 
"Monthly Revenue", 
"Ride Type Distribution", 
"Revenue KPI" 
) 
) 
# ----------------------------- 
# Ride & Revenue Trend 
# ----------------------------- 
fig.add_trace( 
go.Scatter(x=days, y=rides, mode="lines", name="Total Rides"), 
row=1, col=1 
) 
fig.add_trace( 
go.Scatter(x=days, y=revenue, mode="lines", name="Revenue"), 
row=1, col=1 
) 
# ----------------------------- 
# Ride Distance Scatter 
# ----------------------------- 
fig.add_trace( 
go.Scatter(x=days, y=distance, mode="markers", name="Distance (km)"), 
row=2, col=1 
) 
# ----------------------------- 
# Monthly Revenue Aggregation 
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
# Ride Type Pie Chart 
# ----------------------------- 
fig.add_trace( 
go.Pie( 
labels=ride_types, 
values=ride_type_share, 
hole=0.4 
), 
row=3, col=1 
) 
# ----------------------------- 
# KPI Gauge (Revenue Target) 
# ----------------------------- 
target = 500000 
fig.add_trace( 
go.Indicator( 
mode="gauge+number+delta", 
value=np.sum(revenue), 
delta={'reference': target}, 
gauge={ 
'axis': {'range': [0, 1000000]}, 
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
dict(label="Only Rides", 
method="update", 
args=[{"visible": [True, False, False, False, False, 
False]}]), 
dict(label="Only Revenue", 
method="update", 
args=[{"visible": [False, True, False, False, False, 
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
# Range Slider 
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
title=" Uber Ride Analytics Dashboard", 
template="plotly_dark" 
) 
fig.show()