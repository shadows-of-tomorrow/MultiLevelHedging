import QuantLib as ql
from curves.constructors.base import CurveConstructor


class EUR1MCurveConstructor(CurveConstructor):

    def __init__(self) -> None:
        ticker_mask = ["EUR1M_1", "EUR1M_2", "EUR1M_3", "EUR1M_4", "EUR1M_5", "EUR1M_6"]
        super(EUR1MCurveConstructor, self).__init__(ticker_mask)

    def _construct_rate_helpers(self, quotes: dict) -> list:
        rate_helpers = [
            ql.DepositRateHelper(ql.QuoteHandle(quotes["EUR1M_1"]), ql.Period(1, ql.Months), self.settlement_days, self.calendar,
                                 ql.Following, False, self.day_counter),
            ql.DepositRateHelper(ql.QuoteHandle(quotes["EUR1M_2"]), ql.Period(2, ql.Months), self.settlement_days, self.calendar,
                                 ql.Following, False, self.day_counter),
            ql.DepositRateHelper(ql.QuoteHandle(quotes["EUR1M_3"]), ql.Period(3, ql.Months), self.settlement_days, self.calendar,
                                 ql.Following, False, self.day_counter),
            ql.DepositRateHelper(ql.QuoteHandle(quotes["EUR1M_4"]), ql.Period(4, ql.Months), self.settlement_days, self.calendar,
                                 ql.Following, False, self.day_counter),
            ql.DepositRateHelper(ql.QuoteHandle(quotes["EUR1M_5"]), ql.Period(5, ql.Months), self.settlement_days, self.calendar,
                                 ql.Following, False, self.day_counter),
            ql.DepositRateHelper(ql.QuoteHandle(quotes["EUR1M_6"]), ql.Period(6, ql.Months), self.settlement_days, self.calendar,
                                 ql.Following, False, self.day_counter)]
        return rate_helpers
