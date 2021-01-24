from datetime import datetime
from alpha_vantage.client import Client
from alpha_vantage.models import MetadataModel, TimeSeriesModel, TimeSerieModel


class TimeSeries:
    """Initialize TimeSeries class for retrieving data from the various timeseries endpoints.

    :param client: API client instance.
    :type client: alpha_vantage.client.Client
    :param symbol: stock ticker object, for example IBM.
    :type symbol: str
    :param outputsize: compact or full, defaults to compact.
    :type outputsize: str
    :param datatype: class or dataframe, defaults to class.
    :type datatype: str
    """

    def __init__(self, client: Client, symbol: str, outputsize: str = "compact", datatype: str = "class"):
        """Constructor method
        """
        self.client = client
        self.url_append = f"symbol={symbol}&outputsize={outputsize}&datatype=json"

    def __process__(self, data: dict, metadata: dict, format: str):
        """Processes input and returns a TimeSeriesModel instance.

        :param data: dict of dict, containing time series data.
        :type data: dict
        :param metadata: dict containing metadata from response, including symbol and timezone.
        :type metadata: dict
        :param format: format for parsing datetime strings to datetime objects.
        :type format: str
        :return: instance of a TimeSeriesModel, including a list of TimeSerieModel data and metadata.
        :rtype: alpha_vantage.models.TimeSeriesModel
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
        """Retrieve stock data on a daily level.

        :return: an instance of a TimeSeriesModel, containing the requested stock data and metadata.
        :rtype: alpha_vantage.models.TimeSeriesModel
        """
        url = f"?function=TIME_SERIES_DAILY&{self.url_append}"
        data = self.client.get(url=url).json()
        return self.__process__(data[f"Time Series (Daily)"], metadata=data["Meta Data"], format="%Y-%m-%d")

    def intraday(self, interval: str, adjusted: bool = True):
        """Retrieve stock data on a intradaily level.

        :param interval: interval between the historical data points. Allowed values are 1min, 5min, 15min, 30min,
            60min.
        :type interval: str
        :param adjusted: if True, the output time series is adjusted by historical split and dividend events.
        :type adjusted: bool
        :return: an instance of a TimeSeriesModel, containing the requested stock data and metadata.
        :rtype: alpha_vantage.models.TimeSeriesModel
        """
        if interval not in ['1min', '5min', '15min', '30min', '60min']:
            raise ValueError("Invalid input for parameter interval. Allowed values are 1min, 5min, 15min, 30min, 60min")

        url = f"?function=TIME_SERIES_INTRADAY&adjusted={str(adjusted).lower()}&{self.url_append}"
        data = self.client.get(url=url).json()
        return self.__process__(data=data[f"Time Series ({interval})"], metadata=data["Meta Data"], format="%Y-%m-%d %H:%M:%S")