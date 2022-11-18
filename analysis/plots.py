import plotly.graph_objects as go
from plotly.subplots import make_subplots
import analysis.data_merge as merged


class PortfolioPlot:
    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Basic candlestick plot using date, open, high, low, and close.
    fig.add_trace(
        go.Candlestick(x=merged.df_merged['Date'], open=merged.df_merged['Open'], high=merged.df_merged['High'],
                       low=merged.df_merged['Low'], close=merged.df_merged['Close']),
        secondary_y=False)

    # Plot the 21 and 200 day moving averages as new traces on the plotly chart.
    fig.add_trace(go.Scatter(x=merged.df_merged['Date'], y=merged.df_merged['21dma'], line=dict(color='#000000'),
                             name="21-Day-MA"),
                  secondary_y=False)
    fig.add_trace(go.Scatter(x=merged.df_merged['Date'], y=merged.df_merged['200dma'], line=dict(color='#000000'),
                             name="200-Day-MA"),
                  secondary_y=False)

    # Add trace for relative valuation compared to S&P500 index.
    fig.add_trace(go.Scatter(x=merged.df_merged['Date'], y=merged.df_merged['sp500_rel'], line=dict(color='#ADD8E6'),
                             name="Rel-Value-SP500"), secondary_y=True)

    fig.show()
