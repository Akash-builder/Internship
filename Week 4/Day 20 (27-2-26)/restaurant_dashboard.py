import pandas as pd 
import numpy as np 
import seaborn as sns 
import plotly.express as px 
from dash import Dash, html, dcc 
# ========================= 
# LOAD DATA 
# ========================= 
 
df = sns.load_dataset("tips") 
df["tip_pct"] = (df["tip"] / df["total_bill"]) * 100 
 
# ========================= 
# KPI CALCULATIONS 
# ========================= 
 
total_revenue = df["total_bill"].sum() 
total_tips = df["tip"].sum() 
avg_tip_pct = df["tip_pct"].mean() 
avg_bill = df["total_bill"].mean() 
 
peak_day = df.groupby("day", observed=False)["total_bill"].sum().idxmax() 
peak_time = df.groupby("time", observed=False)["total_bill"].sum().idxmax() 
 
# ========================= 
# AGGREGATIONS 
# ========================= 
 
rev_day = df.groupby("day", observed=False)["total_bill"].sum().reset_index() 
rev_time = df.groupby("time", 
observed=False)["total_bill"].sum().reset_index() 
rev_gender = df.groupby("sex", 
observed=False)["total_bill"].sum().reset_index() 
rev_size = df.groupby("size", 
observed=False)["total_bill"].sum().reset_index() 
rev_day_time = df.groupby(["day", "time"], 
observed=False)["total_bill"].sum().reset_index() 
 
# ========================= 
# FIGURES 
# ========================= 
 
fig_day = px.bar(rev_day, x="day", y="total_bill", color="day", 
                 title="Revenue by Day") 
 
fig_time = px.bar(rev_time, x="time", y="total_bill", color="time", 
                  title="Revenue by Time") 
 
fig_tip_dist = px.histogram(df, x="tip_pct", nbins=20, 
                            title="Tip Percentage Distribution") 
 
fig_bill_tip = px.scatter(df, x="total_bill", y="tip", 
                          color="time", 
                          title="Total Bill vs Tip") 
 
fig_gender = px.bar(rev_gender, x="sex", y="total_bill", 
                    color="sex", 
                    title="Revenue by Gender") 
 
fig_size = px.bar(rev_size, x="size", y="total_bill", 
                  title="Revenue by Size") 
 
fig_day_time = px.bar(rev_day_time, x="day", y="total_bill", 
                      color="time", barmode="group", 
                      title="Revenue by Day & Time") 
 
# ========================= 
# DASH APP 
# ========================= 
 
app = Dash(__name__) 
 
# Card style MUST be defined before layout 
card_style = { 
    "backgroundColor": "#f9f9f9", 
    "padding": "20px", 
    "borderRadius": "10px", 
    "boxShadow": "2px 2px 10px rgba(0,0,0,0.1)", 
    "textAlign": "center" 
} 
 
app.layout = html.Div([ 
 
    html.H1("Restaurant Business Dashboard", 
            style={"textAlign": "center"}), 
 
    # KPI GRID 
    html.Div([ 
        html.Div([html.H4("Total Revenue"), 
                  html.H2(f"${total_revenue:,.2f}")], style=card_style), 
 
        html.Div([html.H4("Total Tips"), 
                  html.H2(f"${total_tips:,.2f}")], style=card_style), 
 
        html.Div([html.H4("Average Tip %"), 
                  html.H2(f"{avg_tip_pct:.2f}%")], style=card_style), 
 
        html.Div([html.H4("Average Bill"), 
                  html.H2(f"${avg_bill:.2f}")], style=card_style), 
 
        html.Div([html.H4("Peak Revenue Day"), 
                  html.H2(peak_day)], style=card_style), 
 
        html.Div([html.H4("Peak Revenue Time"), 
html.H2(peak_time)], style=card_style), 
], style={ 
"display": "grid", 
"gridTemplateColumns": "repeat(3, 1fr)", 
"gap": "20px", 
"padding": "20px" 
}), 
# Charts 
dcc.Graph(figure=fig_day), 
dcc.Graph(figure=fig_time), 
dcc.Graph(figure=fig_tip_dist), 
dcc.Graph(figure=fig_bill_tip), 
dcc.Graph(figure=fig_gender), 
dcc.Graph(figure=fig_size), 
dcc.Graph(figure=fig_day_time) 
]) 
if __name__ == "__main__": 
    app.run(debug=True)