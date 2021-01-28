from datetime import datetime
from collections.abc import Sequence

class MetadataModel:
    def __init__(self, symbol: str, last_refreshed: datetime, timezone: str):
        self.symbol = symbol
        self.last_refreshed = last_refreshed
        self.timezone = timezone

    def get_dict(self):
        return {
            "symbol": self.symbol,
            "last_refreshed": self.last_refreshed,
            "timezone": self.timezone
        }



class TimeSerieModel:
    def __init__(self, timestamp: datetime, open: float, high: float, low: float, close: float, volume: int):
        self.timestamp = timestamp
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume

    def get_dict(self):
        return {
            "timestamp": self.timestamp,
            "open": self.open,
            "high": self.high,
            "low": self.low,
            "close": self.close,
            "volume": self.volume
        }


class TimeSeriesModel:
    def __init__(self, series_data: Sequence[TimeSerieModel], metadata: MetadataModel):
        self.metadata = metadata
        self.timeseries = series_data

    def get_list(self):
        return [{**row.get_dict(), **self.metadata.get_dict()} for row in self.timeseries]
