from dash import Dash, html, dcc
import plotly.express as px

app = Dash(__name__)

fig = px.bar(x=["A","B"], y=[10,20])

app.layout = html.Div([
    html.H1("Sales Dashboard"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)