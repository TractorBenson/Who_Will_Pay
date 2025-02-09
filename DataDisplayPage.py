import tkinter as tk
from Page import Page
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from dataDisplay import DataDisplay

### Display Data
class DataDisplayPage(Page):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        label = tk.Label(self, text="Data Display")
        label.pack(pady=10)

        self.data_display = DataDisplay()

    def update_page(self):
        if hasattr(self, "canvas"):
            self.canvas.get_tk_widget().pack_forget()
            self.canvas.get_tk_widget().destroy()
        self.data_display.update_page()
        self.canvas = FigureCanvasTkAgg(self.data_display.fig, self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH)