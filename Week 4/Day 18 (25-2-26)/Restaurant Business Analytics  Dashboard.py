import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import numpy as np

np.random.seed(42)

# ---------------------------
# Create Synthetic Restaurant Data
# ---------------------------
dates = pd.date_range("2024-01-01", "2024-12-31")

restaurants = ["Spicy Hub", "Urban Bites", "Food Fiesta"]
locations = ["Hyderabad", "Bangalore", "Mumbai"]
items = ["Burger", "Pizza", "Pasta", "Biryani", "Sandwich"]

data = []

for restaurant in restaurants:
    for location in locations:
        for date in dates:
            item = np.random.choice(items)
            quantity = np.random.randint(10, 100)
            price = np.random.randint(100, 400)

            sales = quantity * price
            profit = sales * np.random.uniform(0.15, 0.35)

            data.append({
                "Date": date,
                "Restaurant": restaurant,
                "Location": location,
                "Item": item,
                "Quantity": quantity,
                "Sales": round(sales, 2),
                "Profit": round(profit, 2)
            })

df = pd.DataFrame(data)

# ---------------------------
# Create Dash App
# ---------------------------
app = dash.Dash(__name__)
app.title = "RESTAURANT BUSINESS DASHBOARD"

app.layout = html.Div([

    html.H1(
        "RESTAURANT ANALYTICS DASHBOARD",
        style={'textAlign': 'center'}
    ),

    html.Div([

        dcc.Dropdown(
            id='restaurant-dropdown',
            options=[{'label': r, 'value': r} for r in df['Restaurant'].unique()],
            value='Spicy Hub',
            clearable=False,
            style={'width': '30%', 'display': 'inline-block'}
        ),

        dcc.Dropdown(
            id='location-dropdown',
            options=[{'label': l, 'value': l} for l in df['Location'].unique()],
            value='Hyderabad',
            clearable=False,
            style={'width': '30%', 'display': 'inline-block', 'marginLeft': '3%'}
        ),

        dcc.DatePickerRange(
            id='date-picker',
            start_date=df['Date'].min(),
            end_date=df['Date'].max(),
            style={'marginLeft': '3%'}
        )

    ]),

    html.Br(),

    html.Div(
        id='profit-kpi-card',
        style={
            'padding': '20px',
            'width': '30%',
            'textAlign': 'center',
            'fontSize': '20px',
            'borderRadius': '10px',
            'backgroundColor': '#f4f4f4',
            'margin': 'auto'
        }
    ),

    html.Br(),

    dcc.Graph(id='sales-line-chart'),
    dcc.Graph(id='quantity-bar-chart')

])

# ---------------------------
# Callback
# ---------------------------
@app.callback(
    Output('sales-line-chart', 'figure'),
    Output('quantity-bar-chart', 'figure'),
    Output('profit-kpi-card', 'children'),
    Input('restaurant-dropdown', 'value'),
    Input('location-dropdown', 'value'),
    Input('date-picker', 'start_date'),
    Input('date-picker', 'end_date')
)

def update_dashboard(selected_restaurant, selected_location, start_date, end_date):

    filtered = df[
        (df['Restaurant'] == selected_restaurant) &
        (df['Location'] == selected_location) &
        (df['Date'] >= start_date) &
        (df['Date'] <= end_date)
    ]

    # Sales Trend
    sales_fig = px.line(
        filtered,
        x="Date",
        y="Sales",
        title="Sales Trend"
    )

    # Quantity Trend
    quantity_fig = px.bar(
        filtered,
        x="Date",
        y="Quantity",
        title="Quantity Sold"
    )

    # Profit KPI
    total_profit = filtered["Profit"].sum()
    kpi_text = f"Total Profit: ₹{total_profit:,.2f}"

    return sales_fig, quantity_fig, kpi_text

# ---------------------------
# Run App
# ---------------------------
if __name__ == "__main__":
    app.run(debug=True)