import pandas as pd

def max_drawdown(equity: pd.Series) -> float:
    """Worst peak-to-trough drop, as a negative fraction.
    [1000, 1200, 900, 1300] should give -0.25."""
    running_max = equity.cummax()
    drawdown = equity / running_max - 1
    return float(drawdown.min())

if __name__ == "__main__":
    sample = pd.Series([1000, 1200, 900, 1300])
    print(max_drawdown(sample))   # expect -0.25