from requests import Session
from urllib.parse import urljoin


class Client(Session):
    def __init__(self, api_key: str):
        """
        Sets up basic Alpha Vantage client for making requests.

        :param api_key: API key from Alpha Vantage
        """
        if len(api_key) < 10:
            raise ValueError("Invalid value for parameter: api_key")

        self.prefix_url = "https://www.alphavantage.co/query"
        self.api_key = api_key
        super(Client, self).__init__()

    def request(self, method, parameters, *args, **kwargs):
        """
        Returns requests response object

        :param method: GET, POST, PUT, PATH or DELETE
        :param parameters: path after the base URL
        :param args:
        :param kwargs:
        :return: requests response object
        """
        url = urljoin(self.prefix_url, f"{parameters}&apikey={self.api_key}")
        print(url)
        return super(Client, self).request(method, url, *args, **kwargs)
