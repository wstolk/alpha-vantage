# Alpha Vantage Python

```python
from alpha_vantage import Client
from alpha_vantage.functions import TimeSeries

client = Client("API_TOKEN")
ts = TimeSeries(client=client)

daily = ts.daily("IBM")

```