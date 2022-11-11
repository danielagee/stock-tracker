# Day 54 - Merge yfinance and Portfolio Data for Total Portfolio Value
# 1) Import portfolio (quantity of stocks owned) from a .csv.
# 2) Merge yfinance and portfolio data.
# 3) Export to CSV to check.

import yfinance as yf
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

# Read the CSV file containing the stock ticker data.
df_portfolio = pd.read_csv(f'c:\\python\\stocks\\portfolio.csv')

stock = 'GOOGL'  # Input the ticker for the stock you want to view.
ticker = yf.Ticker(stock)  # Gets the correct stock ticker data.
# Download 5 years of data and use actual rather than adjusted prices and reset_index() to add proper index column
df_ticker = ticker.history(period='max', auto_adjust=False).reset_index()

# Label the date column as date-time format in pandas to manage the merges properly.
df_portfolio['Date'] = pd.to_datetime(df_portfolio['Date'])
df_ticker['Date'] = pd.to_datetime(df_ticker['Date'])

# Strip the time out of date-time so that only dates remain
# https://www.golinuxcloud.com/pandas-to-datetime-examples/
df_portfolio['Date'] = df_portfolio['Date'].dt.date
df_ticker['Date'] = df_ticker['Date'].dt.date

# Merge the dataframes using pd.merge()
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html
# https://medium.com/analytics-vidhya/how-to-pd-merge-two-data-frames-on-a-common-date-column-e7808d7ccaee
df_merged = pd.merge(df_ticker, df_portfolio, how='outer')

# Sort the new dataframe by date
# https://www.geeksforgeeks.org/how-to-sort-a-pandas-dataframe-by-date/
df_merged = df_merged.sort_values(by='Date')

# Reset the index of the dataframe without adding a column
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reset_index.html
df_merged = df_merged.reset_index(drop=True)

df_merged.to_csv(f'c:\\python\\stocks\\merged.csv')

"""
df_ticker['21dma'] = df_ticker['Close'].rolling(window=21).mean()  # Calculate 21 day moving average from close price.
df_ticker['200dma'] = df_ticker['Close'].rolling(window=200).mean()  # Calculate 200 day moving average from close price.

sp500_index = '^GSPC'  # Ticker for the S&P 500.
sp500_ticker = yf.Ticker(sp500_index)
df_sp500 = sp500_ticker.history(period='5y', auto_adjust=False).reset_index()

# Calculate relative valuation
df_ticker['sp500_rel'] = df_ticker['Close'] / df_sp500['Close']

# Create figure with secondary y-axis
fig = make_subplots(specs=[[{"secondary_y": True}]])

# Basic candlestick plot using date, open, high, low, and close.
fig.add_trace(go.Candlestick(x=df_ticker['Date'], open=df_ticker['Open'], high=df_ticker['High'],
              low=df_ticker['Low'], close=df_ticker['Close']),
              secondary_y=False)

# Plot the 21 and 200 day moving averages as new traces on the plotly chart.
fig.add_trace(go.Scatter(x=df_ticker['Date'], y=df_ticker['21dma'], line=dict(color='#000000'), name="21-Day-MA"),
              secondary_y=False)
fig.add_trace(go.Scatter(x=df_ticker['Date'], y=df_ticker['200dma'], line=dict(color='#000000'), name="200-Day-MA"),
              secondary_y=False)

# Add trace for relative valuation compared to S&P500 index.
fig.add_trace(go.Scatter(x=df_ticker['Date'], y=df_ticker['sp500_rel'], line=dict(color='#ADD8E6'), name="Rel-Value-SP500"),
              secondary_y=True)

fig.show()
"""