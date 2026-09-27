# Technical Project Documentation

> **Developer & Author:** Penugonda Manoj Mithra  
> **Email:** penugondamanojmithra@gmail.com  
> **Internship:** 1-Month Internship in Python Programming at [VaultofCodes.in](https://vaultofcodes.in)  
> **Academic Context:** Developed by me at this formative stage of my undergraduate computer science academics to transition classroom theoretical principles into modular, industry-grade software applications.

---

## Table of Contents

1. [Project 1: Personal Expense Tracker](#1-project-1-personal-expense-tracker)
   - [Academic Context & Purpose](#11-academic-context--purpose)
   - [Technical Specifications & Architecture](#12-technical-specifications--architecture)
   - [Functional Description](#13-functional-description)
   - [Complete Source Code](#14-complete-source-code)
2. [Project 2: Secret Code Generator (Caesar Cipher)](#2-project-2-secret-code-generator-caesar-cipher)
   - [Academic Context & Purpose](#21-academic-context--purpose)
   - [Technical Specifications & Algorithmic Logic](#22-technical-specifications--algorithmic-logic)
   - [Functional Description](#23-functional-description)
   - [Complete Source Code](#24-complete-source-code)

---

## 1. Project 1: Personal Expense Tracker

### 1.1 Academic Context & Purpose
- **Curriculum Module:** Mini Project — Assignment 3
- **Developed by Me:** Penugonda Manoj Mithra
- **Purpose of this Project:**
  At this stage of my academics, my objective was to master state management, persistent storage, and data visualization in Python. I recognized the practical challenge students face in tracking daily expenses and managing a monthly budget. I developed this application to solve that problem: a clean, interactive command-line expense tracker that records daily spending, persists data safely in `expenses.json`, generates multi-dimensional financial summaries (total, by category, and daily over time), allows in-place record editing and deletion, and plots visual distribution charts using Matplotlib.

### 1.2 Technical Specifications & Architecture
- **Language:** Python 3
- **Primary Modules & Libraries:**
  - `json`: Structured file serialization and deserialization
  - `os`: File existence verification and system checks
  - `datetime`: Automated transaction date generation and date handling
  - `matplotlib.pyplot`: Categorical expense distribution pie charting
- **Data Model:** A list of dictionaries, where each entry represents an expense:
  ```python
  {
      "amount": float,
      "category": str,
      "date": str  # Format: YYYY-MM-DD
  }
  ```

### 1.3 Functional Description

| Function | Parameters | Return Type | Description |
| :--- | :--- | :--- | :--- |
| `load_expenses()` | None | `list` | Reads and deserializes expenses from `expenses.json`. Returns an empty list `[]` if the file does not exist. |
| `save_expenses(expenses)` | `expenses: list` | `None` | Serializes the expense list to `expenses.json` with 4-space formatted indentation. |
| `add_expense(expenses)` | `expenses: list` | `None` | Prompts user for expense amount, category, and date (defaults to today's date if omitted). Appends record and saves to file. |
| `view_summary(expenses)` | `expenses: list` | `None` | Computes and outputs total expenditure, category-wise breakdown, and daily spending over time. |
| `delete_expense(expenses)` | `expenses: list` | `None` | Displays indexed expenses and allows the user to select and delete an entry from storage. |
| `edit_expense(expenses)` | `expenses: list` | `None` | Displays indexed records and allows the user to update amount, category, or date for any entry. |
| `plot_graph(expenses)` | `expenses: list` | `None` | Aggregates categorical spending and renders an interactive pie chart via Matplotlib. |
| `main()` | None | `None` | Main interactive CLI menu loop offering options 1 through 6 with robust input validation. |

### 1.4 Complete Source Code

```python
import json
import os
from datetime import datetime
import matplotlib.pyplot as plt

FILE_NAME = "expenses.json"

# -------------------- File Handling --------------------
def load_expenses():
    """Loads expenses from the local JSON file. Returns an empty list if file doesn't exist."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r', encoding='utf-8') as file:
            return json.load(file)
    return []

def save_expenses(expenses):
    """Saves the expenses list to the local JSON file with formatted indentation."""
    with open(FILE_NAME, 'w', encoding='utf-8') as file:
        json.dump(expenses, file, indent=4)

# -------------------- Core Functions --------------------
def add_expense(expenses):
    """Prompts user to input expense details (amount, category, date) and stores it."""
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category (Food, Transport, Entertainment, etc.): ").capitalize()
        date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
        date = date_input if date_input else datetime.now().strftime('%Y-%m-%d')

        expense = {"amount": amount, "category": category, "date": date}
        expenses.append(expense)
        save_expenses(expenses)
        print("Expense added successfully!\n")
    except ValueError:
        print("Invalid amount. Please try again.\n")

def view_summary(expenses):
    """Displays total spending, categorical breakdown, and daily expenditure summary."""
    if not expenses:
        print("No expenses recorded yet.\n")
        return

    print("--- Expense Summary ---")
    total = sum(exp['amount'] for exp in expenses)
    print(f"Total Spending: ${total:.2f}")

    category_totals = {}
    for exp in expenses:
        category_totals[exp['category']] = category_totals.get(exp['category'], 0) + exp['amount']

    print("\nSpending by Category:")
    for cat, amt in category_totals.items():
        print(f"{cat}: ${amt:.2f}")

    daily_totals = {}
    for exp in expenses:
        daily_totals[exp['date']] = daily_totals.get(exp['date'], 0) + exp['amount']

    print("\nSpending Over Time (Daily):")
    for date, amt in sorted(daily_totals.items()):
        print(f"{date}: ${amt:.2f}")
    print()

def delete_expense(expenses):
    """Displays recorded expenses and allows the user to delete a specific entry."""
    if not expenses:
        print("No expenses to delete.\n")
        return

    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['date']} - {exp['category']} - ${exp['amount']:.2f}")

    try:
        choice = int(input("Enter the number of the expense to delete: "))
        if 1 <= choice <= len(expenses):
            removed = expenses.pop(choice - 1)
            save_expenses(expenses)
            print(f"Deleted expense: {removed}\n")
        else:
            print("Invalid choice.\n")
    except ValueError:
        print("Invalid input.\n")

def edit_expense(expenses):
    """Displays recorded expenses and allows the user to modify amount, category, or date."""
    if not expenses:
        print("No expenses to edit.\n")
        return

    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['date']} - {exp['category']} - ${exp['amount']:.2f}")

    try:
        choice = int(input("Enter the number of the expense to edit: "))
        if 1 <= choice <= len(expenses):
            exp = expenses[choice - 1]
            new_amount = input(f"Enter new amount (current: {exp['amount']}): ")
            new_category = input(f"Enter new category (current: {exp['category']}): ")
            new_date = input(f"Enter new date (current: {exp['date']}): ")

            exp['amount'] = float(new_amount) if new_amount else exp['amount']
            exp['category'] = new_category.capitalize() if new_category else exp['category']
            exp['date'] = new_date if new_date else exp['date']

            save_expenses(expenses)
            print("Expense updated successfully!\n")
        else:
            print("Invalid choice.\n")
    except ValueError:
        print("Invalid input.\n")

def plot_graph(expenses):
    """Visualizes categorical expense distribution as a Matplotlib pie chart."""
    if not expenses:
        print("No data to plot.\n")
        return

    category_totals = {}
    for exp in expenses:
        category_totals[exp['category']] = category_totals.get(exp['category'], 0) + exp['amount']

    plt.figure(figsize=(6, 6))
    plt.pie(category_totals.values(), labels=category_totals.keys(), autopct='%1.1f%%')
    plt.title('Expense Distribution by Category')
    plt.show()

# -------------------- Main Menu --------------------
def main():
    """Main execution loop providing the CLI interactive menu."""
    expenses = load_expenses()

    while True:
        print("==== Personal Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Edit Expense")
        print("4. Delete Expense")
        print("5. Show Graph")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_summary(expenses)
        elif choice == '3':
            edit_expense(expenses)
        elif choice == '4':
            delete_expense(expenses)
        elif choice == '5':
            plot_graph(expenses)
        elif choice == '6':
            print("Exiting... Have a great day!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
```

---

## 2. Project 2: Secret Code Generator (Caesar Cipher)

### 2.1 Academic Context & Purpose
- **Curriculum Module:** Quild Build Module
- **Developed by Me:** Penugonda Manoj Mithra
- **Purpose of this Project:**
  At this stage of my computer science academics, gaining a foundational understanding of cryptography and algorithmic information security was essential. I developed this application to implement and explore the mathematical principles of symmetric substitution ciphers through the Caesar Cipher. The project gave me hands-on practice in modular arithmetic, byte-level character encoding/decoding via ASCII tables, preserving case sensitivity, and building an interactive CLI tool with comprehensive input error handling.

### 2.2 Technical Specifications & Algorithmic Logic
- **Language:** Python 3 (Pure standard library)
- **Mathematical Formulations:**
  - **Encryption Shift:**
    $$E_n(x) = (x + n) \pmod{26}$$
  - **Decryption Inverse Shift:**
    $$D_n(x) = (x - n) \pmod{26}$$
- **ASCII Offsets:**
  - Uppercase alphabet base: `ord('A') = 65`
  - Lowercase alphabet base: `ord('a') = 97`
  - Non-alphabetic symbols (whitespace, punctuation, numbers) are passed through unaltered.

### 2.3 Functional Description

| Function | Parameters | Return Type | Description |
| :--- | :--- | :--- | :--- |
| `encode(message, shift)` | `message: str`, `shift: int` | `str` | Encodes plaintext by shifting each alphabetical character forward by `shift` places along the alphabet while wrapping around using modulo 26. |
| `decode(message, shift)` | `message: str`, `shift: int` | `str` | Inverses the shift operation by shifting characters backward by `shift` places modulo 26, restoring plaintext. |
| `menu()` | None | `None` | Interactive CLI menu loop allowing the user to encode, decode, or exit, with input validation for numeric shifts. |

### 2.4 Complete Source Code

```python
# -------------------- FUNCTIONS --------------------

def encode(message, shift):
    """Encodes the given message by shifting letters forward by 'shift'."""
    result = ""
    for char in message:
        if char.isalpha():  # Process only letters
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # Keep spaces/punctuation unchanged
    return result


def decode(message, shift):
    """Decodes the given message by shifting letters backward by 'shift'."""
    result = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result


def menu():
    """Displays menu and handles user input."""
    while True:
        print("\n=== Secret Code Generator ===")
        print("1. Encode a Message")
        print("2. Decode a Message")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            msg = input("Enter the message to encode: ")
            try:
                shift = int(input("Enter shift value (e.g., 2): "))
                encoded = encode(msg, shift)
                print(f"\nEncoded Message: {encoded}\n")
            except ValueError:
                print("Invalid shift value. Please enter a number.")

        elif choice == '2':
            msg = input("Enter the message to decode: ")
            try:
                shift = int(input("Enter shift value (e.g., 2): "))
                decoded = decode(msg, shift)
                print(f"\nDecoded Message: {decoded}\n")
            except ValueError:
                print("Invalid shift value. Please enter a number.")

        elif choice == '3':
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")


# -------------------- MAIN PROGRAM --------------------
if __name__ == "__main__":
    menu()
```
