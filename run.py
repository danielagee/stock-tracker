
import yfinance as yf
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import datetime

# Read the CSV file containing the stock ticker data.
df_portfolio = pd.read_csv(f'c:\\python\\stocks\\portfolio input\\portfolio.csv')

start_date = datetime.datetime.now() - datetime.timedelta(days=365*15)  # Start date is 15 years ago
end_date = datetime.date.today() - datetime.timedelta(days=0)  # End date is today

stock = 'GOOGL'  # Input the ticker for the stock you want to view.
ticker = yf.Ticker(stock)  # Gets the correct stock ticker data.
# Use actual rather than adjusted prices and reset_index() to add proper index column
df_ticker = ticker.history(start=start_date, end=end_date, auto_adjust=False).reset_index()

sp500_ticker = yf.Ticker('^GSPC')  # Ticker for the S&P 500.
df_sp500 = sp500_ticker.history(start=start_date, end=end_date, auto_adjust=False).reset_index()

# Label the date column as date-time format in pandas to manage the merges properly.
df_portfolio['Date'] = pd.to_datetime(df_portfolio['Date'])
df_ticker['Date'] = pd.to_datetime(df_ticker['Date'])

# Strip the time out of date-time so that only dates remain
df_portfolio['Date'] = df_portfolio['Date'].dt.date
df_ticker['Date'] = df_ticker['Date'].dt.date

# Merge the dataframes using pd.merge()
df_merged = pd.merge(df_ticker, df_portfolio, how='outer')

# Sort the new dataframe by date and reset the index of the dataframe without adding a column
df_merged = df_merged.sort_values(by='Date').reset_index(drop=True)

# convert NaN to value from row above
df_merged.Qty.fillna(method='pad', inplace=True)

# convert NaN to 0
df_merged.Qty.fillna(0, inplace=True)

# Create a new column and get close price x quantity owned.
df_merged['Value'] = df_merged.Close * df_merged.Qty

# Drop all rows without a stock price to give continuous data
df_merged.dropna(inplace=True)

df_ticker['21dma'] = df_ticker['Close'].rolling(window=21).mean()  # Calculate 21 day moving average from close price.
df_ticker['200dma'] = df_ticker['Close'].rolling(window=200).mean()  # Calculate 200 day MA from close price.

# Calculate relative valuation
df_ticker['sp500_rel'] = df_ticker['Close'] / df_sp500['Close']

df_merged.to_csv(f'c:\\python\\stocks\\merged.csv')

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
fig.add_trace(go.Scatter(x=df_ticker['Date'], y=df_ticker['sp500_rel'], line=dict(color='#ADD8E6'),
                         name="Rel-Value-SP500"), secondary_y=True)

fig.show()
