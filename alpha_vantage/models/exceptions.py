class AuthenticationError(Exception):
    """Exception raised when an authentication error with the Alpha Vantage API occured.

    :param message: Error message, has a default descriptive value.
    :type message: str
    """

    def __init__(self, message="Authentication error with the Alpha Vantage API, please validate your API key."):
        self.message = message
        super().__init__(self.message)
