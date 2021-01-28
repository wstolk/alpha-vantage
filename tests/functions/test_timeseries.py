import unittest
import os

from alpha_vantage import Client
from alpha_vantage.functions import TimeSeries
from alpha_vantage.models import TimeSeriesModel
from pandas import DataFrame


class TimeSeriesTestCase(unittest.TestCase):
    def setup(self, datatype="class"):
        key = os.getenv("ALPHA_VANTAGE_API_KEY")
        client = Client(api_key=key)
        ts = TimeSeries(client=client, symbol="IBM", datatype=datatype)
        return ts

    def test_init(self):
        ts = self.setup()
        self.assertIsInstance(ts, TimeSeries)
        ts.client.close()

    def test_daily(self):
        ts = self.setup()
        self.assertIsInstance(ts.daily(), TimeSeriesModel)
        ts.client.close()

    def test_daily_pandas(self):
        ts = self.setup(datatype="pandas")
        daily_df = ts.daily()
        print(daily_df.head())
        self.assertIsInstance(daily_df, DataFrame)
        ts.client.close()

if __name__ == '__main__':
    unittest.main()
