# Day 52 - Add relative valuation to S&P500. https://marketsmith.investors.com/stock-charts/stock-chart-analysis/

import yfinance as yf
import plotly.graph_objects as go
from plotly.subplots import make_subplots

stock = 'GOOGL'  # Input the ticker for the stock you want to view.
ticker = yf.Ticker(stock)  # Gets the correct stock ticker data.
# Download 5 years of data and use actual rather than adjusted prices and reset_index() to add proper index column
df = ticker.history(period='5y', auto_adjust=False).reset_index()

df['21dma'] = df['Close'].rolling(window=21).mean()  # Calculate 21 day moving average from close price.
df['200dma'] = df['Close'].rolling(window=200).mean()  # Calculate 200 day moving average from close price.

sp500_index = '^GSPC'  # Ticker for the S&P 500.
sp500_ticker = yf.Ticker(sp500_index)
df_sp500 = sp500_ticker.history(period='5y', auto_adjust=False).reset_index()

# Calculate relative valuation
df['sp500_rel'] = df['Close'] / df_sp500['Close']

# Create figure with secondary y-axis
fig = make_subplots(specs=[[{"secondary_y": True}]])

# Basic candlestick plot using date, open, high, low, and close.
fig.add_trace(go.Candlestick(x=df['Date'], open=df['Open'], high=df['High'],
              low=df['Low'], close=df['Close']),
              secondary_y=False)

# Plot the 21 and 200 day moving averages as new traces on the plotly chart.
fig.add_trace(go.Scatter(x=df['Date'], y=df['21dma'], line=dict(color='#000000'), name="21-Day-MA"),
              secondary_y=False)
fig.add_trace(go.Scatter(x=df['Date'], y=df['200dma'], line=dict(color='#000000'), name="200-Day-MA"),
              secondary_y=False)

# Add trace for relative valuation compared to S&P500 index.
fig.add_trace(go.Scatter(x=df['Date'], y=df['sp500_rel'], line=dict(color='#ADD8E6'), name="Rel-Value-SP500"),
              secondary_y=True)

fig.show()
