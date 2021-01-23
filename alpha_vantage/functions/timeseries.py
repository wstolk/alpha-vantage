from datetime import datetime
from alpha_vantage.client import Client
from alpha_vantage.models import MetadataModel, TimeSeriesModel, TimeSerieModel


class TimeSeries:
    def __init__(self, client: Client, symbol: str, outputsize: str = "compact", datatype: str = "class"):
        """
        Initialize TimeSeries class for retrieving data from the various timeseries endpoints.

        :param client: alpha_vantage.client.Client instance
        :param symbol: stock ticker object, for example IBM
        :param outputsize: compact or full, defaults to compact
        :param datatype: class or dataframe, defaults to class
        """
        self.client = client
        self.url_append = f"symbol={symbol}&outputsize={outputsize}&datatype=json"

    def __process__(self, data: dict, metadata: dict, format: str):
        """
        processes input and returns a TimeSeriesModel instance.

        :param data: dict of dict, containing time series data
        :param metadata: dict containing metadata from response, including symbol and timezone
        :param format: format for parsing datetime strings to datetime objects
        :return: TimeSeriesModel
        """
        result = []
        metadata = MetadataModel(
            symbol=metadata["2. Symbol"],
            last_refreshed=datetime.strptime(metadata["3. Last Refreshed"], format),
            timezone=metadata["6. Time Zone"] if "6. Time Zone" in metadata else metadata["5. Time Zone"]
        )

        for key in data:
            result.append(TimeSerieModel(
                timestamp=datetime.strptime(key, format),
                open=float(data[key]["1. open"]),
                high=float(data[key]["2. high"]),
                low=float(data[key]["3. low"]),
                close=float(data[key]["4. close"]),
                volume=int(data[key]["5. volume"])
            ))

        return TimeSeriesModel(metadata=metadata, series_data=result)

    def daily(self):
        url = f"?function=TIME_SERIES_DAILY&{self.url_append}"
        data = self.client.get(url=url).json()
        return self.__process__(data[f"Time Series (Daily)"], metadata=data["Meta Data"], format="%Y-%m-%d")

    def intraday(self, interval: str, adjusted: bool = True):
        if interval not in ['1min', '5min', '15min', '30min', '60min']:
            raise ValueError("Invalid input for parameter interval. Allowed values are 1min, 5min, 15min, 30min, 60min")

        url = f"?function=TIME_SERIES_INTRADAY&adjusted={str(adjusted).lower()}&{self.url_append}"
        data = self.client.get(url=url).json()
        return self.__process__(data=data[f"Time Series ({interval})"], metadata=data["Meta Data"], format="%Y-%m-%d %H:%M:%S")