# Personal Expense Tracker

> **Mini Project — Assignment 3**  
> **Author:** Penugonda Manoj Mithra  
> **Email:** penugondamanojmithra@gmail.com  
> **Internship:** Python Programming at [VaultofCodes.in](https://vaultofcodes.in)

---

## 📌 Project Overview

The **Personal Expense Tracker** is a Python CLI application designed to help individuals record, manage, analyze, and visualize their daily financial expenditures. It incorporates fundamental computer science concepts including data persistence using JSON file handling, input validation, date handling, aggregated analytical summaries, and data visualization using Matplotlib.

---

## ✨ Key Features

- **Add Expenses:** Log new transactions with amount, category (e.g., Food, Transport, Entertainment), and timestamp (defaults to current date if omitted).
- **Persistent Data Storage:** Automatic serialization to `expenses.json`, ensuring expenses persist across application sessions.
- **Analytical Summaries:**
  - Overall total spending calculation.
  - Category-wise aggregate spending breakdown.
  - Chronological daily spending breakdown over time.
- **Record Management (CRUD):** Full capability to view, edit existing entries (amount, category, or date), and delete specific expenses.
- **Visual Analytics:** Generates an interactive pie chart visualizing category-wise expense distribution using `matplotlib`.

---

## 🛠️ Tech Stack & Requirements

- **Language:** Python 3.8+
- **Standard Libraries:** `json`, `os`, `datetime`
- **Third-Party Libraries:** `matplotlib`

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run

1. Navigate to the project directory:
   ```bash
   cd 01_Personal_Expense_Tracker
   ```

2. Run the application:
   ```bash
   python expense_tracker.py
   ```

3. Follow the on-screen interactive menu options (1–6).

---

## 📊 Sample Output & Execution

Below are execution screenshots demonstrating the interactive command-line interface, data persistence in `expenses.json`, and graphical pie chart visualization:

### CLI Execution & Expense Analytics Plot
![CLI Output and Expense Graph](../assets/expense_tracker/execution_and_plot.png)

### Persistent Data Storage (`expenses.json`)
![Expenses JSON Storage](../assets/expense_tracker/expenses_json_data.png)

---

## 📂 Source File Structure

```
01_Personal_Expense_Tracker/
├── expense_tracker.py    # Main program source code
├── requirements.txt      # Dependency specifications
└── README.md             # Project documentation
```
