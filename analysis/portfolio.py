
import pandas as pd

# Read the CSV file containing the stock ticker data.
df_portfolio = pd.read_csv(f'c:\\python\\stocks\\portfolio input\\portfolio.csv')

# Label the date column as date-time format in pandas to manage the merges properly.
df_portfolio['Date'] = pd.to_datetime(df_portfolio['Date'])

# Strip the time out of date-time so that only dates remain
df_portfolio['Date'] = df_portfolio['Date'].dt.date
