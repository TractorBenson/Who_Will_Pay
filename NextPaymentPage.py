import tkinter as tk
from Page import Page
import math
import random
import json

### Select Next Payer
class NextPaymentPage(Page):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        label = tk.Label(self, text="Next Payment")
        label.pack(pady=10)

        self.colors = [
            "#3498db",  
            "#e74c3c",  
            "#2ecc71",  
            "#9b59b6",  
            "#f1c40f",  
            "#1abc9c",  
            "#34495e",  
            "#e67e22",   
            "#95a5a6"]
        
    def update_page(self):
        if hasattr(self, "wheel"):
            self.wheel.destroy()
        self.wheel = Wheel(self, self.random_dict(CalculatePosi().get()))
        self.wheel.pack()
        if hasattr(self, "spin_button"):
            self.spin_button.destroy()
        self.spin_button = tk.Button(self, text="Spin", command=self.wheel.spin)
        self.spin_button.pack()

    def random_dict(self, d):
        items = list(d.items())
        random.shuffle(items)
        return dict(items)

class Wheel(tk.Canvas):
    def __init__(self, master, segments:dict, width=400, height=400, **kwargs):
        super().__init__(master, width=width, height=height, bg='white', **kwargs)

        self.segments = segments    #dict name:angle
        self.num_segments = len(segments)
        self.width = width
        self.height = height
        self.center = (width//2, height//2)
        self.radius = min(width, height) // 2 - 20
        self.current_angle = 0
        self.speed = 0
        self.is_spinning = False
        self.colors = random.sample(self.master.colors , self.num_segments)
        self.draw_wheel()

    def draw_wheel(self):
        self.delete("all")
        if self.num_segments == 1:
            self.create_oval(self.center[0]-self.radius, self.center[1]-self.radius, self.center[0]+self.radius, self.center[1]+self.radius,
                             fill=self.colors[0], outline="black")
            self.create_text(self.center[0],self.center[1]-50,text=list(self.segments.keys())[0],font=("Arial", 20, "bold"), fill = "white")
        else: 
            start_angle = self.current_angle
            for i,segment in enumerate(self.segments.keys()):
                color = self.colors[i % len(self.colors)]
                self.create_arc(self.center[0]-self.radius, self.center[1]-self.radius, 
                                self.center[0]+self.radius, self.center[1]+self.radius, 
                                start=start_angle, extent=self.segments[segment], fill=color,
                                outline="black")
                mid_angle = start_angle + self.segments[segment]/2
                rad = math.radians(mid_angle)
                text_x = self.center[0] + self.radius * 0.6 * math.cos(rad)
                text_y = self.center[1] - self.radius * 0.6 * math.sin(rad)
                self.create_text(text_x, text_y, text=segment, font=("Arial", 20, "bold"), fill = "white")
                start_angle += self.segments[segment]

        pointer_size = 15
        self.create_polygon([self.center[0]-pointer_size, self.center[1]-self.radius-20,
                            self.center[0]+pointer_size, self.center[1]-self.radius-20,
                            self.center[0], self.center[1]-self.radius-5], fill="red")
        
    def spin(self, duration = 3000):
        if self.is_spinning:
            return
        if not self.segments:
            return
        self.is_spinning = True
        self.speed = random.uniform(25, 50)
        self.elapsed_time = 0
        self.duration = duration
        self._animate_spin()

    def _animate_spin(self):
        dt = 30 #ms
        self.elapsed_time += dt

        self.current_angle = (self.current_angle + self.speed) % 360
        self.draw_wheel()

        ### logrithmic decrease in speed
        deceletation = random.uniform(0.96, 0.99)
        self.speed *= deceletation

        if self.speed <= 0.1:
            # stop spinning
            self.is_spinning = False
            self.speed = 0
            self.determinate_winner()
        else:
            self.after(dt, self._animate_spin)

    def determinate_winner(self):
        pointer_angle = 90
        effective_angle = (pointer_angle - self.current_angle) % 360
        for i, segment in enumerate(self.segments.keys()):
            if effective_angle < self.segments[segment]:
                winner = segment
                break
            effective_angle -= self.segments[segment]

        self.create_text(self.center[0], self.center[1],
                         text=f"Payer: {winner}", font=("Arial", 20, "bold"), fill = "white")

class CalculatePosi():
    def __init__(self):
        with open("data.json", "r") as f:
            data = json.load(f)
        records = {}
        for person in data:
            records[person["name"]] = 0
            for pays in person["records"]:
                records[person["name"]] += float(pays["amount"])

        with open("settings.json", "r") as file:
            self.penalty_exponent = float(json.load(file)["penalty_exponent"])

        zero_records = []
        for people in records.keys():
            if records[people] == 0:
                zero_records.append(people)
        if len(zero_records) == len(records):
            for item in records.keys():
                records[item] = 1
        elif len(zero_records) == 0:
            for item in records.keys():
                records[item] = (1 / records[item]) ** self.penalty_exponent
        else:
            records = {}
            for item in zero_records:
                records[item] = 1

        s = sum(records.values())
        for item in records.keys():
            records[item] = records[item] / s * 360
        self.records = records

    def get(self):
        return self.records