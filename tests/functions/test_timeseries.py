import unittest
import os

from alpha_vantage import Client
from alpha_vantage.functions import TimeSeries
from alpha_vantage.models import TimeSeriesModel


class TimeSeriesTestCase(unittest.TestCase):
    def setup(self):
        key = os.getenv("ALPHA_VANTAGE_API_KEY")
        client = Client(api_key=key)
        ts = TimeSeries(client=client, symbol="IBM")
        return ts

    def test_init(self):
        ts = self.setup()
        self.assertIsInstance(ts, TimeSeries)
        ts.client.close()

    def test_daily(self):
        ts = self.setup()
        self.assertIsInstance(ts.daily(), TimeSeriesModel)
        ts.client.close()

if __name__ == '__main__':
    unittest.main()
