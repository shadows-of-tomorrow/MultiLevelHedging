import os
import yaml
import QuantLib as ql


class QuoteManager:
    """
    Handles market data feeds containing quotes.
    The quotes are translated to QuantLib quote objects,
    which means that any change is automatically propagated through the system.
    """

    def __init__(self) -> None:
        """
        The constructor generates a nested dictionary where the level-1 key
        denotes the ticker symbol and the level-2 keys denote the fields.
        """
        self.config = self._load_quote_config()
        self.quotes = self._initialize_quotes()

    def _adjust_quote(self, ticker: str, field: str, value: float) -> None:
        self.quotes[ticker][field].setValue(value)

    def _initialize_quotes(self) -> dict:
        """
        Initialize quotes dict with zero simple quotes.
        These will get updated as new market data comes in.
        """
        quotes = {}
        for ticker, fields in self.config.items():
            quotes[ticker] = {}
            for field in fields:
                quotes[ticker][field] = ql.SimpleQuote(0.0)
        return quotes

    def _load_quote_config(self) -> dict:
        config_path = self._construct_config_path()
        with open(config_path, "r") as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                raise Exception(exc)

    def _construct_config_path(self) -> str:
        config_path = os.path.dirname(__file__)
        config_path = os.path.dirname(config_path)
        config_path = os.path.join(config_path, 'io', 'input', 'config_quote.yaml')
        return config_path
