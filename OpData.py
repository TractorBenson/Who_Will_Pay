import json

class AddData:
    def __init__(self, person:str, amount:float, time:str):
        self.record = {
            "amount": amount,
            "time": time,
        }

        with open("data.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            
        for persons in data:
            if persons["name"] == person:
                persons["records"].append(self.record)
                break
        else:
            data.append({"name": person, "records": []})
            data[-1]["records"].append(self.record)

        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)