import pandas as pd
import numpy as np

"""Worst peak-to-trough drop, as a negative fraction.
    [1000, 1200, 900, 1300] should give -0.25."""
def max_drawdown(equity: pd.Series) -> float:
    running_max = equity.cummax()
    drawdown = equity / running_max - 1
    return float(drawdown.min())

"""Annualized Sharpe ratio: mean return / std of returns, scaled to a year.
    (8760 = hours in a year, since our bars are hourly. Vol scales with the sqrt of time.)"""
def sharpe_ratio(equity: pd.Series, periods_per_year:int = 8760) -> float:
    returns = equity.pct_change().dropna()
    mean_return = returns.mean()
    std_return = returns.std()
    return float((mean_return / std_return) * np.sqrt(periods_per_year))

"""Annualized Sortino ratio: mean return / downside deviation, scaled to a year.
    Like Sharpe, but only negative returns count as risk."""
def sortino_ratio(equity: pd.Series, periods_per_year:int = 8760) -> float:
    returns = equity.pct_change().dropna()
    mean_return = returns.mean()
    std_return = returns.std()
    downside_returns = returns[returns < 0]
    if downside_returns.size < 2:
        return 0.0
    downside_deviation = downside_returns.std()
    return float((mean_return / downside_deviation) * np.sqrt(periods_per_year))

if __name__ == "__main__":
    sample = pd.Series([1000, 1200, 900, 1300])
    print(f"Max drawdown: {max_drawdown(sample):.2f}")

if __name__ == "__main__":
    sample = pd.Series([1000, 1200, 900, 1300])
    print(f"Sharpe ratio: {sharpe_ratio(sample):.2f}")

if __name__ == "__main__":
    sample = pd.Series([1000, 1200, 900, 1300])
    print(f"Sortino ratio: {sortino_ratio(sample):.2f}")