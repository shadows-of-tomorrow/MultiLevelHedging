from gui.pages.base import CurvePage


class EURONPage(CurvePage):

    def __init__(self, parent, controller) -> None:
        super(EURONPage, self).__init__(parent, controller, "EURON", "EURON")


class EUR1MPage(CurvePage):

    def __init__(self, parent, controller) -> None:
        super(EUR1MPage, self).__init__(parent, controller, "EUR1M", "EUR1M")


class EUR6MPage(CurvePage):

    def __init__(self, parent, controller) -> None:
        super(EUR6MPage, self).__init__(parent, controller, "EUR6M", "EUR6M")
