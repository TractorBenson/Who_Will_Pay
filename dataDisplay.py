import matplotlib.pyplot as plt
import json

class DataDisplay:
    def __init__(self):
        self.fig, self.ax = plt.subplots(1, 2, figsize=(10, 5))
        self.fig.suptitle("Data Display")
        self.total_payments = 0
        self.average_payment = 0

    def update_page(self):
        with open("data.json", "r") as file:
            data = json.load(file)
            names = []
            nums = []
            amounts = []
            i = 0
            for persons in data:
                if not persons["records"]:
                    continue
                names.append(persons["name"])
                nums.append(0)
                amounts.append(0)
                for payment in persons["records"]:
                    nums[i] += 1
                    amounts[i] += float(payment["amount"])
                i += 1

        self.total_payments = round(sum(amounts),2)
        if sum(nums) == 0:
            self.average_payment = 0
        else:
            self.average_payment = round(self.total_payments / sum(nums), 2)
        self.number_of_meals = sum(nums)

        self.ax[0].clear()
        self.ax[1].clear()
        for text in list(self.fig.texts):
            text.remove()

        self.ax[0].set_title("Number of Payments", fontdict={"fontsize": 8})
        self.ax[1].set_title("Amount of Payments", fontdict={"fontsize": 8})
        self.ax[0].pie(nums, labels=names, autopct=self.make_autopct(nums,0), textprops={"fontsize": 5})
        self.ax[1].pie(amounts, labels=names, autopct=self.make_autopct(amounts,2), textprops={"fontsize": 5})
        self.fig.text(0.5, 0.10, f"Total Payments: {self.total_payments}", ha="center", fontsize=8)
        self.fig.text(0.5, 0.06, f"Number of Meals: {self.number_of_meals}", ha="center", fontsize=8)
        self.fig.text(0.5, 0.02, f"Average Payment: {self.average_payment}", ha="center", fontsize=8)

    def make_autopct(self, values, decimal):
        def my_autopct(pct):
            total = sum(values)
            val = round(pct * total / 100.0, decimal)
            if decimal == 0:
                fval = f"{int(val)}"
            else:
                fval = f"{val:.{decimal}f}"
            return f"{pct:.1f}%\n({fval})"
        return my_autopct