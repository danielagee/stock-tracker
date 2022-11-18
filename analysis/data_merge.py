
import pandas as pd
import analysis.portfolio as portfolio
import analysis.yfinance_import as yf_data

# Merge the dataframes using pd.merge()
df_merged = pd.merge(yf_data.df_ticker, portfolio.df_portfolio, how='outer')

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

# Calculate 21 & 200 day moving averages from close price.
df_merged['21dma'] = yf_data.df_ticker['Close'].rolling(window=21).mean()
df_merged['200dma'] = yf_data.df_ticker['Close'].rolling(window=200).mean()

# Calculate relative valuation
df_merged['sp500_rel'] = yf_data.df_ticker['Close'] / yf_data.df_sp500['Close']

df_merged.to_csv(f'c:\\python\\stocks\\merged.csv')
