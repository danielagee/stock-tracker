# Fix formatting of plots.
# Fix code so that if refresh of stocks is on, it only pulls it once. Currently scrapes both in single and multi plot.
# Enable switch on/off for single and multi-plot

from analysis.plots_single_stock import PortfolioSinglePlots
from analysis.plots_multi_stock import PortfolioCumulativePlot


def run():
    PortfolioSinglePlots()
    PortfolioCumulativePlot()


if __name__ == '__main__':
    run()
