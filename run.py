# Enable switch on/off for single and multi-plot
# Fix value of 100% loss on sell
# Fix relative S&P500 performance calculation.
# Add dividends and sales as returns rather than invested. Invested dividends are not double counted.
# Clean up constants.py code

from analysis.plots_multi_stock import PortfolioCumulativePlot
from analysis.plots_single_stock import PortfolioSinglePlots


def run():
    PortfolioCumulativePlot()
    PortfolioSinglePlots()


if __name__ == '__main__':
    run()
