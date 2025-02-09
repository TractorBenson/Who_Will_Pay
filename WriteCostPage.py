import tkinter as tk
import OpData
from Page import Page
from datetime import date
import json

### Write New Assumption
class WriteCostPage(Page):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        label = tk.Label(self, text="Write Cost")
        label.pack(pady=10)

        with open("settings.json", "r") as file:
            self.names = json.load(file)["names"]
        ### Option Menu
        self.selected_option = tk.StringVar()
        self.selected_option.set("(Not Selected)")
        option_menu = tk.OptionMenu(self, self.selected_option,"(Not Selected)", *self.names)
        option_menu.pack(padx=10, pady=30)

        ###  AmountEntry
        amount_label = tk.Label(self, text="Amount:")
        amount_label.pack(pady=0)
        self.entry_amount = tk.Entry(self)
        self.entry_amount.pack(padx=10, pady=0)

        ### TimeEntry
        holder_label = tk.Label(self, text="")
        holder_label.pack(pady=15)
        time_label = tk.Label(self, text="Time: yyyy-mm-dd")
        time_label.pack(pady=0)
        self.entry_time = tk.Entry(self)
        self.entry_time.pack(padx=10, pady=0)


        ### Submit Button
        submit_button = tk.Button(self, text="Submit", command=lambda: self.submit_data(self.selected_option.get(), self.entry_amount.get(), self.entry_time.get()))
        submit_button.pack(pady=30)

    def update_page(self):
        self.selected_option.set("(Not Selected)")
        self.entry_amount.delete(0, tk.END)
        self.entry_time.delete(0, tk.END)
        self.entry_time.insert(0, f"{date.today()}")
        if hasattr(self, "suc"):
            self.suc.destroy()
        if hasattr(self, "warn"):
            self.warn.destroy()
    
    def submit_data(self, person, amount, time):
        if hasattr(self, "warn"):
            self.warn.destroy()
        if hasattr(self, "suc"):
            self.suc.destroy()
        
        if person == "(Not Selected)":
            self.warn = tk.Label(self, text="Please select a person")
            self.warn.pack()
            return 0
        if not amount:
            self.warn = tk.Label(self, text="Please enter an amount")
            self.warn.pack()
            return 0
        if not time:
            self.warn = tk.Label(self, text="Please enter a time")
            self.warn.pack()
            return 0
        try:
            amount = float(amount)
        except ValueError:
            self.warn = tk.Label(self, text="Amount must be a number")
            self.warn.pack()
            return 0
        OpData.AddData(person, amount, time)
        
        self.entry_amount.delete(0, tk.END)
        self.entry_time.delete(0, tk.END)
        self.suc = tk.Label(self, text="Data successfully added!")
        self.suc.pack()