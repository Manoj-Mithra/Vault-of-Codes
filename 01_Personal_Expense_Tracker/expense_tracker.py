"""
Personal Expense Tracker
Author: Penugonda Manoj Mithra
Email: penugondamanojmithra@gmail.com
Internship: VaultofCodes.in - Python Programming

Description:
A modular Python CLI application that allows users to record, categorize,
summarize, edit, delete, and visualize their daily expenses with JSON file persistence.
"""

import json
import os
from datetime import datetime
try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None


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
    if plt is None:
        print("Error: 'matplotlib' is not installed.")
        print("Please install dependencies with: pip install -r requirements.txt\n")
        return

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
