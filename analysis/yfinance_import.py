
import yfinance as yf
import pandas as pd
import datetime

start_date = datetime.datetime.now() - datetime.timedelta(days=365*15)  # Start date is 15 years ago
end_date = datetime.date.today() - datetime.timedelta(days=0)  # End date is today

stock = 'GOOGL'  # Input the ticker for the stock you want to view.
ticker = yf.Ticker(stock)  # Gets the correct stock ticker data.
# Use actual rather than adjusted prices and reset_index() to add proper index column
df_ticker = ticker.history(start=start_date, end=end_date, auto_adjust=False).reset_index()

sp500_ticker = yf.Ticker('^GSPC')  # Ticker for the S&P 500.
df_sp500 = sp500_ticker.history(start=start_date, end=end_date, auto_adjust=False).reset_index()

# Label the date column as date-time format in pandas to manage the merges properly.
df_ticker['Date'] = pd.to_datetime(df_ticker['Date'])

# Strip the time out of date-time so that only dates remain
df_ticker['Date'] = df_ticker['Date'].dt.date
