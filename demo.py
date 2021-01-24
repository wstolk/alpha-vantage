import os

from alpha_vantage import Client
from alpha_vantage.functions import TimeSeries


if __name__ == "__main__":
    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    client = Client(api_key)
    ts = TimeSeries(client=client, symbol="IBM")
    daily = ts.daily()

    for day in daily.timeseries:
        print(f"{daily.metadata.symbol} high for {day.timestamp.date()}: {day.high}")
