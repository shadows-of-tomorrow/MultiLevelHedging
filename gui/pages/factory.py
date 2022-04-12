from gui.pages.base import Page
from gui.pages.general import HomePage, CurveMonitor
from gui.pages.curves import EURONPage, EUR1MPage, EUR6MPage


class PageFactory(object):

    @staticmethod
    def create_page(parent, controller, page_id: str) -> Page:
        if page_id == "Home":
            return HomePage(parent, controller)
        elif page_id == "EURON":
            return EURONPage(parent, controller)
        elif page_id == "EUR1M":
            return EUR1MPage(parent, controller)
        elif page_id == "EUR6M":
            return EUR6MPage(parent, controller)
        elif page_id == "Curves":
            return CurveMonitor(parent, controller)
        else:
            raise ValueError(f"Page id: {page_id} not recognized!")