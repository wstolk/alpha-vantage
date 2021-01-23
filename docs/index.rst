.. alpha-vantage documentation master file, created by
   sphinx-quickstart on Sat Jan 23 21:12:12 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Alpha-Vantage API Python wrapper!
=========================================

**alpha_vantage: stock market data for your project**::

    >>> from alpha_vantage import Client
    >>> from alpha_vantage.functions import TimeSeries
    >>> client = Client(api_key="abcdefg123")
    >>> ts = TimeSeries(symbol="IBM")
    >>> daily = ts.daily()
    >>> daily.metadata.symbol
    'IBM'
    >>> daily.metadata.timezone
    'Europe/Amsterdam'
    >>> daily.timeseries[0].high
    127.39
    >>> daily.timeseries[0].timestamp
    datetime.datetime(2021, 1, 20, 12, 30, 0, 000000)



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
