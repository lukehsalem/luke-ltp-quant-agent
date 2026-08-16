import requests
import pandas as pd
import numpy as np

"""Fetch real OHLCV klines from Binance's free public API.
    Returns a DataFrame: [timestamp, open, high, low, close, volume].
    Live prices."""
def fetch_binance_klines(symbol: str = "BTCUSDT", interval: str = "1h",
                        limit: int = 1000) -> pd.DataFrame:
    url = "https://api.binance.us/api/v3/klines"
    params = {"symbol": symbol, "interval": interval, "limit": limit}

    response = requests.get(url, params=params)
    response.raise_for_status()
    raw = response.json()

    df = pd.DataFrame(raw, columns=[
    "timestamp", "open", "high", "low", "close", "volume",
    "close_time", "quote_volume", "trades",
    "taker_base", "taker_quote", "ignore"])

    df = df[["timestamp", "open", "high", "low", "close", "volume"]]

    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    for col in ["open", "high", "low", "close", "volume"]:
        df[col] = df[col].astype(float)
    
    return df

"""Generate synthetic OHLCV data as a DataFrame matching the Binance schema:
    [timestamp, open, high, low, close, volume].
    Synthetic price - fallback data"""
def generate_synthetic_klines(n_bars: int = 2000, start_price: float = 60000.0,
                              seed: int = 42) -> pd.DataFrame:
    # 1. get a close-price path from generate_close_prices(...)
    # 2. build open/high/low around each close (approximate but realistic)
    # 3. make a timestamp column (a range of hourly datetimes)
    # 4. assemble into a DataFrame with the 6 standard columns and return it

if __name__ == "__main__":
    df = fetch_binance_klines(limit=5)
    print(df)
    print(df.dtypes)

