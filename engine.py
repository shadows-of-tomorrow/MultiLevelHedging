import asyncio
from gui.controller import GUIController
from curves.manager import CurveManager
from quotes.manager import QuoteManager


class Engine:

    def __init__(self):
        self.quote_manager = QuoteManager()
        self.curve_manager = CurveManager(self.quote_manager.quotes)
        self.gui_controller = GUIController(self.curve_manager)

    async def _async_monitor_and_gui(self):
        await asyncio.gather(self.gui_controller.mainloop_async(), self.quote_manager.monitor())

    def run(self):
        asyncio.run(self._async_monitor_and_gui())
