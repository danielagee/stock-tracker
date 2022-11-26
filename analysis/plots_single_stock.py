class PortfolioSinglePlots:
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    import analysis.data_merge as merged
    import analysis.portfolio as portfolio
    import analysis.constants as c
    import pandas as pd

    df_merged = pd.read_csv(f'{c.root_path}3merged_value.csv')
    df_sp500 = pd.read_csv(f'{c.output_path}sp500.csv')

    for ticker in portfolio.tickers:
        # Define the 21 and 200 day moving average calculations from closing price
        df_merged['21dma'] = df_merged[f'Close-{ticker}'].rolling(window=21).mean()
        df_merged['200dma'] = df_merged[f'Close-{ticker}'].rolling(window=200).mean()
        df_merged['sp500_rel'] = df_merged[f'Close-{ticker}'] / df_sp500['Close']

        # Create figure with secondary y-axis
        fig = make_subplots(specs=[[{"secondary_y": True}]])

        # Basic candlestick plot using date, open, high, low, and close.
        fig.add_trace(
            go.Candlestick(x=df_merged['Date'],
                           open=df_merged[f'Open-{ticker}'],
                           high=df_merged[f'High-{ticker}'],
                           low=df_merged[f'Low-{ticker}'],
                           close=df_merged[f'Close-{ticker}'],
                           name=f'{ticker}'),
            secondary_y=False)

        # Plot the 21 and 200 day moving averages as new traces on the plotly chart.
        fig.add_trace(
            go.Scatter(x=df_merged['Date'],
                       y=df_merged['21dma'],
                       line=dict(color='#000000'),
                       name="21-Day-MA"),
            secondary_y=False)
        fig.add_trace(
            go.Scatter(x=df_merged['Date'],
                       y=df_merged['200dma'],
                       line=dict(color='#000000'),
                       name="200-Day-MA"),
            secondary_y=False)

        # Add trace for relative valuation compared to S&P500 index.
        fig.add_trace(
            go.Scatter(x=df_merged['Date'],
                       y=df_merged['sp500_rel'],
                       line=dict(color='#ADD8E6'),
                       name="Rel-Value-SP500"),
            secondary_y=True)

        # Add trace for total returns.
        fig.add_trace(
            go.Scatter(x=df_merged['Date'],
                       y=df_merged[f'Returns-{ticker}'],
                       line=dict(color='#333333'),
                       name=f'Returns-{ticker}'),
            secondary_y=False)

        # Add trace for total returns %.
        fig.add_trace(
            go.Scatter(x=df_merged['Date'],
                       y=df_merged[f'Returns %-{ticker}'],
                       line=dict(color='#555555'),
                       name=f'Returns %-{ticker}'),
            secondary_y=True)

        # Add trace for total dividends received.
        fig.add_trace(
            go.Scatter(x=df_merged['Date'],
                       y=df_merged[f'Total Div-{ticker}'],
                       line=dict(color='#666666'),
                       name=f'Dividends-{ticker}'),
            secondary_y=True)

        fig.show()
