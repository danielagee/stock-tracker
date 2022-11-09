# Day 50 - Build a candlestick plot in plotly
# Install plotly package
# Documentation can be found here:
# https://plotly.com/python/candlestick-charts/

import yfinance as yf
# Import plotly to plot the data as graph objects (go).
import plotly.graph_objects as go

stock = 'GOOGL'  # Input the ticker for the stock you want to view.
ticker = yf.Ticker(stock)  # Gets the correct stock ticker data.
df = ticker.history()  # Downloads historical data for open, high, low, close, volume, dividends, splits to a dataframe.

# The original format uses the date column as the index. As we need an index column for plotly,
# Before we plot, we need to re-index the data set and store the original index (date) as a new column.
df = df.reset_index()

# Basic candlestick plot using date, open, high, low, and close.
fig = go.Figure(data=[go.Candlestick(x=df['Date'], open=df['Open'], high=df['High'],
                                       low=df['Low'], close=df['Close'])])

fig.show()
