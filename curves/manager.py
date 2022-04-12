from datetime import datetime
from curves.constructors.eur1m import EUR1MCurveConstructor
from curves.constructors.eur6m import EUR6MCurveConstructor


class CurveManager:
    """
    Simple class that manages a bunch of curves.
    """

    def __init__(self, quotes: dict) -> None:
        self.curves = self._construct_curves(quotes)

    def get_nodes(self, identifier: str):
        nodes = self.curves[identifier].nodes()
        dates = [datetime(x[0].year(), x[0].month(), x[0].dayOfMonth()) for x in nodes]
        yields = [x[1] for x in nodes]
        return dates, yields

    def _construct_curves(self, quotes: dict) -> dict:
        return {
            "EUR1M": EUR1MCurveConstructor().construct_curve(quotes),
            "EUR6M": EUR6MCurveConstructor().construct_curve(quotes)
        }
