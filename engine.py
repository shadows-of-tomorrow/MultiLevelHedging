import time
import threading
import numpy as np
from gui.gui import HedgeGUI
from curves.manager import CurveManager


class Engine:

    def __init__(self):
        self.curve_manager = CurveManager()
        self.gui = HedgeGUI(self.curve_manager)

    def _curve_mods(self):
        """
        Todo: This should be linked to quote updates.
        :return:
        """
        while True:
            time.sleep(1)
            new_quotes = np.random.normal(0.01, 0.05, size=(len(self.curve_manager.deposit_quotes),))
            k = 0
            for key, value in self.curve_manager.deposit_quotes.items():
                value.setValue(new_quotes[k])
                k += 1

    def _run_curve_thread(self):
        thread = threading.Thread(target=self._curve_mods)
        thread.start()

    def run(self):
        self._run_curve_thread()
        self.gui.mainloop()