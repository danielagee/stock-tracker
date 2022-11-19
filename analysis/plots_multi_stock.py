class PortfolioPlot:
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    import analysis.data_merge as data

    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Line plot for total investments.
    fig.add_trace(
        go.Scatter(
            x=data.df_merged_value['Date'], y=data.df_merged_value['Total Invested'], line=dict(color='#EE4B2B'),
            name="Total Investments", yaxis="y1"
        )
    )

    # Line plot for portfolio value.
    fig.add_trace(
        go.Scatter(
            x=data.df_merged_value['Date'], y=data.df_merged_value['Total Value'], line=dict(color='#ADD8E6'),
            name="Total Portfolio Value", yaxis="y1"
        )
    )

    # Line plot for % returns value.
    fig.add_trace(
        go.Scatter(
            x=data.df_merged_value['Date'], y=data.df_merged_value['Returns %'], line=dict(color='#000000'),
            name="Returns %", yaxis="y2"
        )
    )

    fig.show()
