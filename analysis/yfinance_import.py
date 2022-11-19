
import time
from pandas_datareader import data as pdr

import analysis.constants as c
import analysis.portfolio as portfolio

start_date = c.start_date
end_date = c.end_date

if c.refresh_tickers == "Yes":
    for ticker in portfolio.tickers:
        df = pdr.get_data_yahoo(ticker, start_date, end_date)
        df.to_csv(f'{c.output_path}{ticker}.csv')
        print(f'Ticker: {ticker}')
    #    print(df)
        time.sleep(1)

    df_sp500 = pdr.get_data_yahoo('^GSPC', start_date, end_date)
    df_sp500.to_csv(f'{c.output_path}df_sp500.csv')
    print(f'Ticker: ^GSPC')

    df_dji = pdr.get_data_yahoo('^DJI', start_date, end_date)
    df_sp500.to_csv(f'{c.output_path}df_dji.csv')
    print(f'Ticker: ^DJI')

    df_nasdaq = pdr.get_data_yahoo('^IXIC', start_date, end_date)
    df_sp500.to_csv(f'{c.output_path}df_nasdaq.csv')
    print(f'Ticker: ^IXIC')