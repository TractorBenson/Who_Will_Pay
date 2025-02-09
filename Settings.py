import json
from Page import Page
import tkinter as tk

class Settings(Page):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        with open("data.json","r")as file:
            data = json.load(file)
        with open("settings.json", "r") as file:
            settings = json.load(file)

        expected_names = settings["names"]
        actual_names = []
        for person in data:
            actual_names.append(person["name"])
        for name in expected_names:
            if name not in actual_names:
                data.append(
                    {
                        "name": name,
                        "records": []
                    }
                )
        
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

        label = tk.Label(self, text="Settings")
        label.pack(pady=10)
        
        names_label = tk.Label(self, text="Names:")
        names_label.pack()
        self.names_entry = tk.Entry(self)
        self.names_entry.pack()
        exponent_label = tk.Label(self, text="Penalty Exponent:")
        exponent_label.pack()
        self.exponent_entry = tk.Entry(self)
        self.exponent_entry.pack()

        self.save_button = tk.Button(self, text="Save", command=self.save_settings)
        self.save_button.pack()

    def update_page(self):
        if hasattr(self, "suc"):
            self.suc.destroy()
        if hasattr(self, "warn"):
            self.warn.destroy()
        with open("settings.json", "r") as file:
            data = json.load(file)
            self.names = data["names"]
            self.exponent = data["penalty_exponent"]
        
        self.names_entry.delete(0, tk.END)
        self.exponent_entry.delete(0, tk.END)
        self.names_entry.insert(0, ", ".join(self.names))
        self.exponent_entry.insert(0, self.exponent)

    def save_settings(self):
        names = self.names_entry.get().split(",")
        for i in range(len(names)):
            names[i] = names[i].strip()
        exponent = self.exponent_entry.get()
        try:
            exponent = float(exponent)
        except ValueError:
            if hasattr(self, "warn"):
                self.warn.destroy()
            self.warn = tk.Label(self, text="Please enter a number for the penalty exponent")
            self.warn.pack()
            return 0
        with open("settings.json", "w") as file:
            json.dump({"names": names, "penalty_exponent": exponent}, file, indent=4)
        self.update_page()
        self.suc = tk.Label(self, text="Settings saved")
        self.suc.pack()
