import pandas as pd
import pyodbc

# Example SQL Server connection
conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=localhost;'
    'DATABASE=pizza_db;'
    'UID=your_username;'
    'PWD=your_password'
)

# Fetch data
df = pd.read_sql("SELECT * FROM pizza_sales", conn)

import dash
from dash import dcc, html
import plotly.express as px

app = dash.Dash(__name__)

# Precompute analytics
total_revenue = df['total_price'].sum()
total_orders = df['order_id'].nunique()
total_pizzas = df['quantity'].sum()
avg_order_value = total_revenue / total_orders
avg_pizzas_per_order = total_pizzas / total_orders

# Daily Trends
daily_orders = df.groupby(df['order_date'].dt.day_name())['order_id'].nunique().reset_index()
daily_orders.columns = ['Day', 'Orders']

fig_daily = px.bar(daily_orders, x='Day', y='Orders', title='Daily Orders')

# Monthly Trends
monthly_orders = df.groupby(df['order_date'].dt.month_name())['order_id'].nunique().reset_index()
monthly_orders.columns = ['Month', 'Orders']

fig_monthly = px.bar(monthly_orders, x='Month', y='Orders', title='Monthly Orders')

# Layout
app.layout = html.Div([
    html.H1("Pizza Sales Dashboard"),
    
    html.Div([
        html.P(f"Total Revenue: ${total_revenue:.2f}"),
        html.P(f"Total Orders: {total_orders}"),
        html.P(f"Total Pizzas Sold: {total_pizzas}"),
        html.P(f"Average Order Value: ${avg_order_value:.2f}"),
        html.P(f"Average Pizzas per Order: {avg_pizzas_per_order:.2f}")
    ], style={'padding': 20, 'border': '1px solid black'}),
    
    dcc.Graph(figure=fig_daily),
    dcc.Graph(figure=fig_monthly)
])

if __name__ == '__main__':
    app.run_server(debug=True) 