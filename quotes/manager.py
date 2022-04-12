import os
import csv
import QuantLib as ql

from quotes.api import DummyAPI


class QuoteManager:
    """
    Handles market data feeds containing quotes.
    The quotes are translated to QuantLib quotes objects,
    which means that any change is automatically propagated through the system.
    """

    def __init__(self) -> None:
        """
        The constructor generates a nested dictionary where the level-1 key
        denotes the ticker symbol and the level-2 keys denote the fields.
        """
        self.ticker_dict = self._get_ticker_dict()
        self.tickers = list(self.ticker_dict.keys())
        self.quotes = self._initialize_quotes()
        self.api = DummyAPI(tickers=self.tickers)

    async def monitor(self):
        async for feed_quotes in self.api.feed():
            self._adjust_quotes(feed_quotes)

    def _adjust_quotes(self, feed_quotes: dict) -> None:
        for key, value in feed_quotes.items():
            self.quotes[key].setValue(value)

    def _initialize_quotes(self) -> dict:
        quotes = {}
        for ticker in self.tickers:
            quotes[ticker] = ql.SimpleQuote(0.0)
        return quotes

    def _get_ticker_dict(self) -> dict:
        ticker_dict = {}
        ticker_path = self._get_ticker_path()
        with open(ticker_path) as f:
            header = next(f)
            reader = csv.reader(f)
            for row in reader:
                ticker_dict[row[0]] = [row[1], row[2]]
        return ticker_dict

    def _get_ticker_path(self) -> str:
        ticker_path = os.path.dirname(os.path.dirname(__file__))
        ticker_path = os.path.join(ticker_path, 'io', 'input', 'tickers.csv')
        return ticker_path
