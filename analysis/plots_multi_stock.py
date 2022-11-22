class PortfolioPlot:
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    import analysis.data_merge as data
    import numpy as np

    # Create sub-plot
    fig = make_subplots(rows=2, cols=1,
                        row_heights=[0.8, 0.2],
                        subplot_titles=("Portfolio Value", "Portfolio Returns"))

    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Portfolio Invested & Value (USD)", row=1, col=1)
    fig.update_yaxes(title_text="Return on Investment (%)", row=2, col=1)

    # Line plot for total investments.
    fig.add_trace(go.Scatter(
        x=data.df_merged_value['Date'],
        y=data.df_merged_value['Total Invested'],
        line=dict(color='#EE4B2B'),
        name="Total Investments"),
        row=1, col=1)

    # Line plot for portfolio value.
    fig.add_trace(go.Scatter(
        x=data.df_merged_value['Date'],
        y=data.df_merged_value['Total Value'],
        line=dict(color='#ADD8E6'),
        name="Total Portfolio Value"),
        row=1, col=1)

    # Sub plot for returns

    # Returns plot positive
    fig.add_trace(go.Scatter(
        x=data.df_merged_value['Date'],
        y=np.maximum(0, data.df_merged_value['Returns %']*100),
        marker=dict(size=0),
        line=(dict(color='#046307')),
        fill='tozeroy',
        name="Returns %"),
        row=2, col=1)

    fig.show()
