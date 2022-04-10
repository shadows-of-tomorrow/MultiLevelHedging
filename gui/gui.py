import tkinter as tk
from gui.pages import HomePage, CurvePage


class HedgeGUI(tk.Tk):

    def __init__(self, curve_manager, *args, **kwargs):
        self.curve_manager = curve_manager
        tk.Tk.__init__(self, *args, **kwargs)
        self.container = self._construct_container()
        self.frames = self._construct_frames()
        self.show_frame(HomePage)

    def _construct_frames(self):
        frames = {}
        for page in (HomePage, CurvePage):
            frame = page(self.container, self)
            frames[page] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        return frames

    def _construct_container(self):
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        return container

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
