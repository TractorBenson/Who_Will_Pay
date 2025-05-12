import tkinter as tk
from WriteCostPage import WriteCostPage
from NextPaymentPage import NextPaymentPage
from DataDisplayPage import DataDisplayPage  
from Settings import Settings

import os
import json

# Ensure data file exists with default structure
DATA_FILE = 'data.json'
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)

SETTINGS_FILE = 'settings.json'
DEFAULT_SETTINGS = {
    "names": [],
    "penalty_exponent": 3.0
}

# Ensure settings file exists with default structure
if not os.path.exists(SETTINGS_FILE):
    with open(SETTINGS_FILE, 'w') as f:
        json.dump(DEFAULT_SETTINGS, f, indent=4)

### Main App
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Who Will Pay?") 
        self.geometry("800x600")

        menu_frame = tk.Frame(self)
        menu_frame.pack(side="top", fill="x", pady=0)

        menu_frame.grid_columnconfigure(0, weight=1)
        menu_frame.grid_columnconfigure(1, weight=1)
        menu_frame.grid_columnconfigure(2, weight=1)
        menu_frame.grid_columnconfigure(3, weight=1)

        btn_data_display = tk.Button(menu_frame, text="Display Data", command=lambda: self.show_frame(DataDisplayPage))
        btn_data_display.grid(row=0, column=0)
        btn_next_payment = tk.Button(menu_frame, text="Next Payment", command=lambda: self.show_frame(NextPaymentPage))
        btn_next_payment.grid(row=0, column=1)
        btn_write_cost = tk.Button(menu_frame, text="Write Cost", command=lambda: self.show_frame(WriteCostPage))
        btn_write_cost.grid(row=0, column=2)
        btn_settings = tk.Button(menu_frame, text="Settings", command=lambda: self.show_frame(Settings))
        btn_settings.grid(row=0, column=3)

        content_frame = tk.Frame(self)
        content_frame.pack(side="left", fill="both", expand=True)
        content_frame.grid_rowconfigure(0, weight=1)
        content_frame.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (DataDisplayPage, NextPaymentPage, WriteCostPage, Settings):
            frame = F(content_frame, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(DataDisplayPage)

    def show_frame(self, page_class):
        self.frames[page_class].update_page()
        self.frames[page_class].tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()