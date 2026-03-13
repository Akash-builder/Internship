import numpy as np 
import plotly.graph_objects as go 
from plotly.subplots import make_subplots 
np.random.seed(101) 
# ----------------------------- 
# Generate Synthetic Crypto Data 
# ----------------------------- 
days = 250 
dates = np.arange(days) 
price = np.cumsum(np.random.normal(0, 2, days)) + 500 
open_price = price + np.random.normal(0, 2, days) 
close_price = price + np.random.normal(0, 2, days) 
high_price = np.maximum(open_price, close_price) + np.random.rand(days) * 5 
low_price = np.minimum(open_price, close_price) - np.random.rand(days) * 5 
volume = np.random.randint(5000, 20000, days) 
# ----------------------------- 
# Moving Averages 
# ----------------------------- 
ma20 = np.convolve(close_price, np.ones(20)/20, mode='same') 
ma100 = np.convolve(close_price, np.ones(100)/100, mode='same') 
# ----------------------------- 
# Bollinger Bands 
# ----------------------------- 
rolling_std = np.array([np.std(close_price[max(0,i-20):i+1]) for i in 
range(days)]) 
upper_band = ma20 + (2 * rolling_std) 
lower_band = ma20 - (2 * rolling_std) 
# ----------------------------- 
# RSI Calculation 
# ----------------------------- 
delta = np.diff(close_price, prepend=close_price[0]) 
gain = np.where(delta > 0, delta, 0) 
loss = np.where(delta < 0, -delta, 0) 
avg_gain = np.convolve(gain, np.ones(14)/14, mode='same') 
avg_loss = np.convolve(loss, np.ones(14)/14, mode='same') 
rs = avg_gain / (avg_loss + 1e-10) 
rsi = 100 - (100 / (1 + rs)) 
# ----------------------------- 
# MACD Calculation 
# ----------------------------- 
ema12 = np.convolve(close_price, np.ones(12)/12, mode='same') 
ema26 = np.convolve(close_price, np.ones(26)/26, mode='same') 
macd = ema12 - ema26 
signal = np.convolve(macd, np.ones(9)/9, mode='same') 
# ----------------------------- 
# Create Dashboard Layout 
# ----------------------------- 
fig = make_subplots( 
    rows=4, cols=1, 
    shared_xaxes=True, 
    vertical_spacing=0.03, 
    row_heights=[0.5, 0.15, 0.15, 0.2], 
    subplot_titles=("Crypto Price", "Volume", "RSI Indicator", "MACD Indicator") 
) 
# ----------------------------- 
# Candlestick Chart 
# ----------------------------- 
fig.add_trace( 
go.Candlestick( 
x=dates, 
open=open_price, 
high=high_price, 
low=low_price, 
close=close_price, 
name="Candlestick" 
), 
row=1, col=1 
) 
# Moving Averages 
fig.add_trace(go.Scatter(x=dates, y=ma20, mode='lines', name='MA20'), 
row=1, col=1) 
fig.add_trace(go.Scatter(x=dates, y=ma100, mode='lines', name='MA100'), 
row=1, col=1) 
# Bollinger Bands 
fig.add_trace(go.Scatter(x=dates, y=upper_band, mode='lines', name='Upper Band', line=dict(dash='dash')), row=1, col=1) 
fig.add_trace(go.Scatter(x=dates, y=lower_band, mode='lines', name='Lower Band', line=dict(dash='dash')), row=1, col=1) 
# ----------------------------- 
# Volume 
# ----------------------------- 
fig.add_trace( 
go.Bar(x=dates, y=volume, name="Volume"), 
row=2, col=1 
) 
# ----------------------------- 
# RSI 
# ----------------------------- 
fig.add_trace( 
go.Scatter(x=dates, y=rsi, mode='lines', name="RSI"), 
row=3, col=1 
) 
fig.add_hline(y=70, line_dash="dash", row=3, col=1) 
fig.add_hline(y=30, line_dash="dash", row=3, col=1) 
# ----------------------------- 
# MACD 
# ----------------------------- 
fig.add_trace(go.Scatter(x=dates, y=macd, mode='lines', name="MACD"), 
row=4, col=1) 
fig.add_trace(go.Scatter(x=dates, y=signal, mode='lines', name="Signal"), 
row=4, col=1) 
# ----------------------------- 
# Layout Settings 
# ----------------------------- 
fig.update_layout( 
height=1000, 
title="Cryptocurrency Market Analytics Dashboard", 
template="plotly_dark", 
xaxis_rangeslider_visible=False 
) 
fig.show()