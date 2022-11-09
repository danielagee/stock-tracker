# Day 49 - Pull historical stock data with yfinance
# Install yfinance package
# Full documentation can be found here:
# https://pypi.org/project/yfinance/
# https://github.com/ranaroussi/yfinance
# https://aroussi.com/post/python-yahoo-finance
# https://algotrading101.com/learn/yfinance-guide/

import yfinance as yf

stock = 'GOOGL'  # Input the ticker for the stock you want to view.
ticker = yf.Ticker(stock)  # Gets the correct stock ticker data.
df = ticker.history()  # Downloads historical data for open, high, low, close, volume, dividends, splits to a dataframe.

print(df)