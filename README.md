# Alpha Vantage Python

**alpha_vantage** is a simple Python wrapper around the Alpha Vantage API:

```python
from alpha_vantage import Client
from alpha_vantage.functions import TimeSeries

# setup API client and TimeSeries interface for retrieving IBM stock data
client = Client("API_TOKEN")
ts = TimeSeries(client=client, symbol="IBM")

# retrieve historic stock data on a daily level
daily = ts.daily()

# loop over results
for day in daily.timeseries:
    print(f"- {day.timestamp}: {day.high}")

```

## Installation 

alpha_vantage is available on PyPi:

```shell script
$ python -m pip install alpha-vantage-py
```

## Features

* Easy integration with your Python project
* Alpha Vantage endpoints wrapped in functions
