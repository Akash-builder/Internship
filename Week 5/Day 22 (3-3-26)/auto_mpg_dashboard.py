import pandas as pd 
import numpy as np 
import seaborn as sns 
import plotly.express as px 
import plotly.graph_objects as go 
from dash import Dash, html, dcc 
# ========================= 
# LOAD DATA 
# ========================= 
df = sns.load_dataset("mpg") 
# Data Cleaning 
df = df.dropna() 
# Rename columns for clarity 
df.rename(columns={ 
"origin": "Origin", 
"model_year": "Model Year", 
"horsepower": "Horsepower", 
"weight": "Weight", 
"mpg": "MPG", 
"displacement": "Displacement", 
"cylinders": "Cylinders", 
"acceleration": "Acceleration" 
}, inplace=True) 
# ========================= 
# KPI CALCULATIONS 
# ========================= 
total_vehicles = len(df) 
avg_mpg = df["MPG"].mean() 
max_mpg = df["MPG"].max() 
min_mpg = df["MPG"].min() 
avg_hp = df["Horsepower"].mean() 
# MPG YoY Growth 
mpg_by_year = df.groupby("Model Year")["MPG"].mean().reset_index() 
yoy_growth = ((mpg_by_year["MPG"].iloc[-1] - mpg_by_year["MPG"].iloc[0]) 
/ mpg_by_year["MPG"].iloc[0]) * 100 
# Correlations 
corr_matrix = df[["MPG", "Weight", "Horsepower", 
"Displacement", "Cylinders", 
"Acceleration"]].corr() 
mpg_weight_corr = corr_matrix.loc["MPG", "Weight"] 
mpg_hp_corr = corr_matrix.loc["MPG", "Horsepower"] 
# ========================= 
# DASH APP 
# ========================= 
app = Dash(__name__) 
card_style = { 
"backgroundColor": "#f2f2f2", 
"padding": "15px", 
"borderRadius": "10px", 
"textAlign": "center", 
"boxShadow": "2px 2px 8px rgba(0,0,0,0.1)" 
} 
app.layout = html.Div([ 
html.H1("Auto MPG Executive Dashboard", 
style={"textAlign": "center"}), 
# ================= KPI CARDS ================= 
html.Div([ 
html.Div([html.H4("Average MPG"), 
html.H2(f"{avg_mpg:.2f}")], style=card_style), 
html.Div([html.H4("MPG YoY Growth %"), 
html.H2(f"{yoy_growth:.2f}%")], style=card_style), 
html.Div([html.H4("Average Horsepower"), 
html.H2(f"{avg_hp:.2f}")], style=card_style), 
html.Div([html.H4("Total Vehicles"), 
html.H2(total_vehicles)], style=card_style) 
], style={"display": "grid", 
"gridTemplateColumns": "repeat(4, 1fr)", 
              "gap": "15px", 
              "padding": "20px"}), 
 
    # ================= MIDDLE SECTION ================= 
 
    dcc.Graph( 
        figure=px.line( 
            mpg_by_year, 
            x="Model Year", 
            y="MPG", 
            title="Fuel Efficiency Trend (MPG Over Years)", 
            markers=True 
        ) 
    ), 
 
    dcc.Graph( 
        figure=px.bar( 
            df.groupby("Origin")["MPG"].mean().reset_index(), 
            x="Origin", 
            y="MPG", 
            title="Average MPG by Origin" 
        ) 
    ), 
 
    # ================= BOTTOM SECTION ================= 
 
    dcc.Graph( 
        figure=px.scatter( 
            df, 
            x="Weight", 
            y="MPG", 
            title=f"MPG vs Weight (Corr: {mpg_weight_corr:.2f})" 
        ) 
    ), 
 
    dcc.Graph( 
        figure=px.scatter( 
            df, 
            x="Horsepower", 
            y="MPG", 
            title=f"MPG vs Horsepower (Corr: {mpg_hp_corr:.2f})" 
        ) 
    ), 
 
    dcc.Graph( 
        figure=px.histogram( 
            df, 
            x="MPG", 
            nbins=30, 
            title="MPG Distribution" 
        ) 
    ), 
 
    dcc.Graph( 
        figure=px.imshow( 
            corr_matrix, 
            text_auto=True, 
            title="Correlation Matrix" 
        ) 
    ) 
 
]) 
# ========================= 
# RUN APP 
# ========================= 
if __name__ == "__main__": 
    app.run(debug=True)