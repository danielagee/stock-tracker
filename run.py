# Fix code so that if refresh of stocks is on, it only pulls it once. Currently scrapes both in single and multi plot.
# Enable switch on/off for single and multi-plot
# Relative value vs S&P 500 rather than absolute

from analysis.plots_multi_stock import PortfolioCumulativePlot
from analysis.plots_single_stock import PortfolioSinglePlots


def run():
    PortfolioCumulativePlot()
    PortfolioSinglePlots()


if __name__ == '__main__':
    run()
