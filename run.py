# Day 51 - Add 21 and 200 day moving averages.

import yfinance as yf
import plotly.graph_objects as go

stock = 'GOOGL'  # Input the ticker for the stock you want to view.
ticker = yf.Ticker(stock)  # Gets the correct stock ticker data.
# Download 5 years of data and use actual rather than adjusted prices
df = ticker.history(period='5y', auto_adjust=False).reset_index()  # reset_index() to add proper index column

# Define the 21 and 200 day moving average calculations from closing price
df['21dma'] = df['Close'].rolling(window=21).mean()
df['200dma'] = df['Close'].rolling(window=200).mean()

# Basic candlestick plot using date, open, high, low, and close.
fig = go.Figure(data=[go.Candlestick(x=df['Date'], open=df['Open'], high=df['High'],
                                       low=df['Low'], close=df['Close'])])

# Plot the 21 and 200 day moving averages as new traces on the plotly chart.
fig.add_trace(go.Scatter(x=df['Date'], y=df['21dma'], line=dict(color='#000000'), name="21-Day-MA"))
fig.add_trace(go.Scatter(x=df['Date'], y=df['200dma'], line=dict(color='#000000'), name="200-Day-MA"))

fig.show()
