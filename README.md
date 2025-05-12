# Who_Will_Pay v1 (Legacy)

> A lightweight desktop expense tracker built with Python and Tkinter.

---

> **⚠️ Legacy notice:**  
> This is the first implementation (v1.2) using Tkinter and JSON for storage.  
> For the latest web-based version (v2.0) with Flask, SQLite, and Chart.js, see:  
> https://github.com/20age1million/Who-Will-Pay-Expense-Tracker  

---

## Introduction

Who_Will_Pay is a simple group expense tracker that helps friends:

- **Record payments** made by each person  
- **View summaries** of total and per-person spending  
- **Randomly select** who pays next

It runs as a desktop GUI application and stores data in a local JSON file.

---

## Features

- **Summary view** showing grand total and breakdown per person  
- **Weighted Random Picker**  
  Randomly selects the next payer using weights based on each person’s total payments, so that those who have paid less have a higher chance—ensuring fair distribution over time.
- **Add** individual payment entries  
- **Lightweight storage** in a human-readable JSON file  

---

## Built With

- **Python 3.12**  
- **Tkinter** (standard library GUI toolkit)  
- **JSON** (for simple local data persistence)  

---

## Installation & Usage

1. **Clone the repo**  
   ```bash
   git clone https://github.com/TractorBenson/Who_Will_Pay.git
   cd Who_Will_Pay
   ···
2. **Ensure you are on Python 3.12**
   ```bash
   python --version  # should report "Python 3.12.x"
   ```
3. **Run the application**
   ```bash
   python main.py
   ```
4. **Data file**
   - On first run, a **data.json** and **setting.json** will be created in the working directory.
   - You can manually open or edit **data.json** and **setting.json** to inspect or modify stored records and settings—just keep valid JSON syntax.
5. **Usage**
   - On first run, open **Settings** page, enter the names to track (separated by commas), and save.
   - Restart the application. The **Next Payment** and **Write New Payment** pages will now function correctly.
   - The **Data Display** page will become available after recording your first payment on the **Write New Payment** page.
   - The **penalty_exponent** setting controls the weighting for the next payer selection: a higher exponent increases the disparity between participants’ probabilities. 