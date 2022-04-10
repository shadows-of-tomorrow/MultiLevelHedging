import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation


class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Home Page", font=("Verdana", 12))
        label.pack(pady=10, padx=10)

        button = ttk.Button(self, text="Curve Page", command=lambda: controller.show_frame(CurvePage))
        button.pack()


class CurvePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.f, self.a = self._construct_figure()
        self.controller = controller

        label = tk.Label(self, text="Curve Page", font=("Verdana", 12))
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Home Page", command=lambda: controller.show_frame(HomePage))
        button1.pack()

        canvas = FigureCanvasTkAgg(self.f, self)
        canvas.draw()
        self.ani = animation.FuncAnimation(self.f, self._draw_curves, interval=100)
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def _construct_figure(self) -> tuple:
        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)
        return f, a

    def _draw_curves(self, i):
        dates, yields = self.controller.curve_manager.get_nodes()
        self.a.clear()
        self.a.plot(dates, yields)
