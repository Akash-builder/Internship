import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

np.random.seed(303)

# -----------------------------
# Synthetic Blinkit Data
# -----------------------------
days = np.arange(1, 121)
orders = np.random.randint(300, 900, 120)
avg_order_value = np.random.uniform(200, 600, 120)
delivery_time = np.random.uniform(8, 25, 120)

revenue = orders * avg_order_value

# Category Sales %
categories = ["Fruits & Veg", "Dairy", "Snacks", "Beverages", "Personal Care"]
category_share = [30, 20, 20, 15, 15]

# City Revenue %
cities = ["Bangalore", "Delhi", "Mumbai", "Hyderabad"]
city_share = [35, 25, 25, 15]

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
        "Orders & Revenue Trend",
        "Delivery Time Analysis",
        "Monthly Revenue",
        "Category Distribution",
        "Revenue KPI"
    )
)

# -----------------------------
# Orders & Revenue Trend
# -----------------------------
fig.add_trace(
    go.Scatter(x=days, y=orders, mode="lines", name="Orders"),
    row=1, col=1
)

fig.add_trace(
    go.Scatter(x=days, y=revenue, mode="lines", name="Revenue"),
    row=1, col=1
)

# -----------------------------
# Delivery Time Scatter
# -----------------------------
fig.add_trace(
    go.Scatter(x=days, y=delivery_time, mode="markers", name="Delivery Time (min)"),
    row=2, col=1
)

# -----------------------------
# Monthly Revenue Aggregation
# -----------------------------
monthly_rev = np.array_split(revenue, 6)
monthly_sum = [m.sum() for m in monthly_rev]

fig.add_trace(
    go.Bar(
        x=["M1", "M2", "M3", "M4", "M5", "M6"],
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
        labels=categories,
        values=category_share,
        hole=0.4
    ),
    row=3, col=1
)

# -----------------------------
# KPI Gauge (Revenue Target)
# -----------------------------
target = 20000000

fig.add_trace(
    go.Indicator(
        mode="gauge+number+delta",
        value=np.sum(revenue),
        delta={'reference': target},
        gauge={
            'axis': {'range': [0, 40000000]},
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
                dict(
                    label="Show All",
                    method="update",
                    args=[{"visible": [True, True, True, True, True, True]}]
                ),
                dict(
                    label="Only Orders",
                    method="update",
                    args=[{"visible": [True, False, False, False, False, False]}]
                ),
                dict(
                    label="Only Revenue",
                    method="update",
                    args=[{"visible": [False, True, False, False, False, False]}]
                )
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
    title="Blinkit Quick Commerce Analytics Dashboard",
    template="plotly_dark"
)

fig.show()