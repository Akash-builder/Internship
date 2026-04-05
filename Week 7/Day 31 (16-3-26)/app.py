# ================= IMPORTS ================= #
import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# ================= LOAD DATA ================= #
df = pd.read_csv("pizza_sales.csv")

# Convert date
df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True, errors='coerce')

# ================= KPI CALCULATIONS ================= #
total_revenue = df['total_price'].sum()
total_orders = df['order_id'].nunique()
total_pizzas = df['quantity'].sum()
avg_order_value = total_revenue / total_orders
avg_pizzas_per_order = total_pizzas / total_orders

# ================= DATA FOR CHARTS ================= #

# Daily trend
daily_orders = df.groupby(df['order_date'].dt.date)['order_id'].nunique().reset_index()

# Monthly trend
monthly_orders = df.groupby(df['order_date'].dt.month)['order_id'].nunique().reset_index()

# Category sales
category_sales = df.groupby('pizza_category')['total_price'].sum().reset_index()

# Size sales
size_sales = df.groupby('pizza_size')['total_price'].sum().reset_index()

# Category quantity
category_qty = df.groupby('pizza_category')['quantity'].sum().reset_index()

# Top 5
top5 = df.groupby('pizza_name').agg({
    'total_price': 'sum'
}).reset_index().sort_values(by='total_price', ascending=False).head(5)

# Bottom 5
bottom5 = df.groupby('pizza_name').agg({
    'total_price': 'sum'
}).reset_index().sort_values(by='total_price').head(5)

# ================= CREATE FIGURES ================= #
fig_daily = px.bar(daily_orders, x='order_date', y='order_id',
                   title="Daily Orders Trend")

fig_monthly = px.line(monthly_orders, x='order_date', y='order_id',
                      title="Monthly Orders Trend")

fig_category = px.pie(category_sales, names='pizza_category', values='total_price',
                      title="Sales by Category")

fig_size = px.pie(size_sales, names='pizza_size', values='total_price',
                  title="Sales by Size")

fig_qty = px.bar(category_qty, x='pizza_category', y='quantity',
                 title="Quantity by Category")

fig_top5 = px.bar(top5, x='pizza_name', y='total_price',
                  title="Top 5 Pizzas")

fig_bottom5 = px.bar(bottom5, x='pizza_name', y='total_price',
                     title="Bottom 5 Pizzas")

# ================= DASH APP ================= #
app = Dash(__name__)

app.layout = html.Div([
    
    html.H1("Pizza Sales Dashboard", style={'textAlign': 'center'}),

    # ================= KPI SECTION ================= #
    html.Div([
        html.Div([html.H3("Total Revenue"), html.P(f"{total_revenue:.2f}")]),
        html.Div([html.H3("Total Orders"), html.P(f"{total_orders}")]),
        html.Div([html.H3("Total Pizzas Sold"), html.P(f"{total_pizzas}")]),
        html.Div([html.H3("Avg Order Value"), html.P(f"{avg_order_value:.2f}")]),
        html.Div([html.H3("Avg Pizzas/Order"), html.P(f"{avg_pizzas_per_order:.2f}")]),
    ], style={'display': 'flex', 'justifyContent': 'space-around'}),

    # ================= CHARTS ================= #
    dcc.Graph(figure=fig_daily),
    dcc.Graph(figure=fig_monthly),
    dcc.Graph(figure=fig_category),
    dcc.Graph(figure=fig_size),
    dcc.Graph(figure=fig_qty),
    dcc.Graph(figure=fig_top5),
    dcc.Graph(figure=fig_bottom5),

])

# ================= RUN SERVER ================= #
if __name__ == '__main__':
    app.run(debug=True)