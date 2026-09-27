# Technical Project Documentation

This document provides a consolidated technical reference containing complete source codes and functional descriptions for the projects developed during the **Vault of Codes (VOC) Python Programming Internship**.

---

## Table of Contents

1. [Project 1: Personal Expense Tracker](#1-project-1-personal-expense-tracker)
   - [Overview & Specifications](#11-overview--specifications)
   - [Functional Description](#12-functional-description)
   - [Complete Source Code](#13-complete-source-code)
2. [Project 2: Secret Code Generator (Caesar Cipher)](#2-project-2-secret-code-generator-caesar-cipher)
   - [Overview & Specifications](#21-overview--specifications)
   - [Functional Description](#22-functional-description)
   - [Complete Source Code](#23-complete-source-code)

---

## 1. Project 1: Personal Expense Tracker

### 1.1 Overview & Specifications
- **Module:** Mini Project — Assignment 3
- **Primary Goal:** Allow users to log daily financial expenses, store them persistently in a JSON file, compute analytical summaries, manage entries (add, edit, delete), and generate visual distribution charts.
- **Key Python Concepts Applied:**
  - File I/O & JSON Serialization (`json.load`, `json.dump`)
  - Error and Exception Handling (`try-except ValueError`)
  - Date and Time Operations (`datetime.now`)
  - Dictionary and List Data Structures
  - Data Aggregation and Visualization (`matplotlib.pyplot`)

### 1.2 Functional Description

| Function | Parameters | Description |
| :--- | :--- | :--- |
| `load_expenses()` | None | Reads and deserializes expenses from `expenses.json`. If the file does not exist, returns an empty list `[]`. |
| `save_expenses(expenses)` | `expenses: list` | Serializes the list of expense dictionaries into `expenses.json` with 4-space indentation. |
| `add_expense(expenses)` | `expenses: list` | Accepts user inputs for amount, category, and date (defaulting to current date if left empty). Appends record and saves to file. |
| `view_summary(expenses)` | `expenses: list` | Computes and displays the total expenditure, categorical breakdown, and daily spending over time in formatted currency. |
| `delete_expense(expenses)` | `expenses: list` | Lists all expenses with indexed numbers and deletes the user-selected item, followed by updating storage. |
| `edit_expense(expenses)` | `expenses: list` | Displays recorded expenses and allows modifying amount, category, or date for any existing record. |
| `plot_graph(expenses)` | `expenses: list` | Calculates percentage contribution per category and renders an interactive pie chart via Matplotlib. |
| `main()` | None | Orchestrates the command-line menu loop providing options 1 through 6. |

### 1.3 Complete Source Code

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

### 2.1 Overview & Specifications
- **Module:** Quild Build Module
- **Primary Goal:** Provide a modular cryptographic tool that encodes and decodes text using the Caesar Cipher substitution algorithm with custom numeric shifts.
- **Key Python Concepts Applied:**
  - ASCII manipulation via `ord()` and `chr()`
  - Modulo arithmetic (`% 26`) for cyclic alphabet wrapping
  - Case preservation (`isupper()`, `islower()`)
  - Input validation and loop controls

### 2.2 Functional Description

| Function | Parameters | Description |
| :--- | :--- | :--- |
| `encode(message, shift)` | `message: str`, `shift: int` | Converts each alphabetical letter forward by `shift` places, wrapping around using `(ord(char) - base + shift) % 26 + base`. Non-alphabetic characters remain untouched. |
| `decode(message, shift)` | `message: str`, `shift: int` | Inverses the shift operation by shifting letters backward by `shift` places: `(ord(char) - base - shift) % 26 + base`. |
| `menu()` | None | Presents an interactive CLI menu loop allowing users to input messages, enter shift values, view encoded/decoded results, and handle invalid inputs gracefully. |

### 2.3 Complete Source Code

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
