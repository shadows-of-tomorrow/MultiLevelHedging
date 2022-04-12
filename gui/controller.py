import asyncio
import tkinter as tk
from gui.pages.factory import PageFactory

PAGE_LAYOUT = {
    "Home": ["Curves"],
    "Curves": ["Home", "EUR1M", "EUR6M"],
    "EUR1M": ["Home", "Curves"],
    "EUR6M": ["Home", "Curves"]
}


class GUIController(tk.Tk):

    def __init__(self, curve_manager, *args, **kwargs):
        super(GUIController, self).__init__(*args, **kwargs)
        self.curve_manager = curve_manager
        self.page_layout = PAGE_LAYOUT
        self.container = self._construct_container()
        self.pages = self._construct_pages()
        self.show_page("Home")

    async def mainloop_async(self, interval=0.01):
        while True:
            self.update()
            await asyncio.sleep(interval)

    def _construct_pages(self):
        pages = {}
        for page_id in PAGE_LAYOUT.keys():
            page = PageFactory.create_page(self.container, self, page_id)
            pages[page.identifier] = page
            page.grid(row=0, column=0, sticky="nsew")
        pages = self._add_navbars(pages)
        return pages

    def _add_navbars(self, pages) -> dict:
        for original_page, nav_pages in PAGE_LAYOUT.items():
            pages[original_page].add_navbar(nav_pages)
        return pages

    def _construct_container(self) -> tk.Frame:
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        return container

    def show_page(self, page_id: str):
        frame = self.pages[page_id]
        frame.tkraise()
