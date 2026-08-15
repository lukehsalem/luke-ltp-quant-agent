import pandas as pd

def max_drawdown(returns: pd.Series) -> float:
    """Worst peak-to-trough drop, as a negative fraction.
    [1000, 1200, 900, 1300] should give -0.25."""
    running_max = equity.cummax()
    drawdown = equity / running_max - 1
    return float(drawdown.min())