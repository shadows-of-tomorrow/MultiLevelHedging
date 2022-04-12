from typing import List
from abc import abstractmethod
import QuantLib as ql


class CurveConstructor:

    def __init__(self, ticker_mask: List[str]) -> None:
        self.calendar = ql.TARGET()
        self.reference_date = ql.Settings.instance().evaluationDate
        self.settlement_days = 0
        self.day_counter = ql.Actual360()
        self.ticker_mask = ticker_mask

    def construct_curve(self, quotes: dict) -> ql.YieldTermStructure:
        relevant_quotes = self._extract_relevant_quotes(quotes)
        rate_helpers = self._construct_rate_helpers(relevant_quotes)
        return ql.PiecewiseLinearZero(self.reference_date, rate_helpers, self.day_counter)

    def _extract_relevant_quotes(self, quotes: dict) -> dict:
        relevant_quotes = {}
        for k, v in quotes.items():
            if k in self.ticker_mask:
                relevant_quotes[k] = v
        return relevant_quotes

    @abstractmethod
    def _construct_rate_helpers(self, quotes: dict) -> list:
        pass
