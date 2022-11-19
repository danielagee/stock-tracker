import pandas as pd
import datetime

df_portfolio = pd.read_csv(f'c:\\python\\stocks\\portfolio input\\portfolio.csv')
output_path = 'c:\\python\\stocks\\Portfolio Output\\'
start_date = datetime.datetime.now() - datetime.timedelta(days=365*18)  # Start date is 18 years ago
end_date = datetime.date.today() - datetime.timedelta(days=0)  # End date is today
refresh_tickers = "No"
