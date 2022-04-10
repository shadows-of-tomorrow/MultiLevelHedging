import QuantLib as ql
from datetime import datetime


class CurveManager:
    """
    Handles the construction of term structures.
    Due to the observer pattern design of QuantLib curves
    are automatically adjusted if market quotes change.
    """

    def __init__(self) -> None:
        self.calendar = ql.TARGET()
        self.current_date = ql.Date(6, ql.November, 2001)
        ql.Settings.instance().evaluationDate = self.current_date
        self.settlement_days = 0
        self.day_counter = ql.Actual360()
        self.deposit_quotes = self._construct_deposit_quotes()
        self.deposit_helpers = self._construct_deposit_helpers()
        self.term_structure = self._construct_term_structure()

    def get_nodes(self):
        nodes = self.term_structure.nodes()
        dates = [datetime(x[0].year(), x[0].month(), x[0].dayOfMonth()) for x in nodes]
        yields = [x[1] for x in nodes]
        return dates, yields

    def _construct_term_structure(self):
        return ql.PiecewiseLinearZero(self.current_date, self.deposit_helpers, self.day_counter)

    def _construct_deposit_quotes(self) -> dict:
        depo_quotes = {}
        depo_quotes[(1, ql.Days)] = ql.SimpleQuote(0.01)
        depo_quotes[(2, ql.Days)] = ql.SimpleQuote(0.02)
        depo_quotes[(3, ql.Days)] = ql.SimpleQuote(0.03)
        depo_quotes[(4, ql.Days)] = ql.SimpleQuote(0.04)
        depo_quotes[(5, ql.Days)] = ql.SimpleQuote(0.05)
        return depo_quotes

    def _construct_deposit_helpers(self):
        return [
            ql.DepositRateHelper(
                ql.QuoteHandle(self.deposit_quotes[(n, unit)]),
                ql.Period(n, unit),
                self.settlement_days,
                self.calendar,
                ql.ModifiedFollowing,
                False,
                self.day_counter,
            )
            for n, unit in self.deposit_quotes.keys()
        ]