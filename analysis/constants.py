import pandas as pd
import datetime

df_portfolio = pd.read_csv(f'c:\\python\\stocks\\portfolio input\\portfolio - Dividend.csv')
output_path = 'c:\\python\\stocks\\Portfolio Output\\'
root_path = 'c:\\python\\stocks\\'
# start_date = datetime.datetime.now() - datetime.timedelta(days=365*18)  # Start date is 18 years ago, redefined in Portfolio tab.
start_delay = 30  # Start timeline xx days before earliest portfolio acquisition
end_date = datetime.date.today() - datetime.timedelta(days=0)  # End date is today
refresh_tickers = "Yes"
refresh_dividends = "Yes"
portfolio_plot = "Yes"
individual_plot = "Yes"
