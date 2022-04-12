from gui.pages.base import Page


class HomePage(Page):

    def __init__(self, parent, controller) -> None:
        super(HomePage, self).__init__(parent, controller, "Home Page", "Home")


class CurveMonitor(Page):

    def __init__(self, parent, controller) -> None:
        super(CurveMonitor, self).__init__(parent, controller, "Curve Monitor", "Curves")
