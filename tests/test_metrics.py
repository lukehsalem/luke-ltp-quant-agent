import sys
import os
import pytest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import pandas as pd
from metrics import max_drawdown, sharpe_ratio, sortino_ratio, total_return, cagr


def test_max_drawdown():
    equity = pd.Series([1000, 1200, 900, 1300])
    assert max_drawdown(equity) == -0.25

def test_sharpe_ratio():
    equity = pd.Series([1000, 1200, 900, 1300])
    assert sharpe_ratio(equity) > 0

def test_sortino_ratio():
    equity = pd.Series([1000, 1200, 900, 1300])
    assert sortino_ratio(equity) == 0.0

def test_total_return():
    equity = pd.Series([1000, 1200, 900, 1300])
    assert total_return(equity) == pytest.approx(0.3)

def test_cagr():
    equity = pd.Series([1000, 1200, 900, 1300])
    assert cagr(equity) > 0