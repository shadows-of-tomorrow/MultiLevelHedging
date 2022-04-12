from __future__ import annotations

import tkinter as tk
from tkinter import ttk
from typing import List
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

HEADER_FONT = ("Verdana", 12)
FIGURE_SIZE = (5, 5)
FIGURE_ANIMATION_INTERVAL = 100


class Page(tk.Frame):

    def __init__(self, parent: tk.Frame, controller, header_text: str, identifier: str) -> None:
        super(Page, self).__init__(parent)
        self.controller = controller
        self.header_text = header_text
        self.identifier = identifier
        self._construct_header()

    def _construct_header(self) -> None:
        label = tk.Label(self, text=self.header_text, font=HEADER_FONT)
        label.pack(pady=10, padx=10)

    def add_navbar(self, page_ids: List[str]) -> None:
        for page_id in page_ids:
            button = ttk.Button(self, text=page_id, command=lambda x=page_id: self.controller.show_page(x))
            button.pack(side=tk.LEFT, anchor="nw")


class CurvePage(Page):

    def __init__(self, parent, controller, header_text: str, identifier: str) -> None:
        super(CurvePage, self).__init__(parent, controller, header_text, identifier)
        self.figure, self.axes = self._construct_figure()
        self._construct_canvas()

    def _construct_canvas(self) -> None:
        canvas = FigureCanvasTkAgg(self.figure, self)
        canvas.draw()
        self.ani = animation.FuncAnimation(self.figure, self._draw_curves, interval=FIGURE_ANIMATION_INTERVAL)
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    def _draw_curves(self, i) -> None:
        dates, yields = self.controller.curve_manager.get_nodes(self.identifier)
        self.axes.clear()
        self.axes.plot(dates, yields)

    def _construct_figure(self) -> tuple:
        figure = Figure(figsize=FIGURE_SIZE, dpi=100)
        figure.tight_layout()
        axes = figure.add_subplot(111)
        return figure, axes