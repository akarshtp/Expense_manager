import numpy as np
import matplotlib.pyplot as plt

# Initialize an empty array for expenses
expenses = np.array([], dtype=[('date', 'U10'), ('category', 'U20'), ('description', 'U50'), ('amount', 'f8')])

def add_expense(date, category, description, amount):
    global expenses
    new_expense = np.array([(date, category, description, amount)], dtype=expenses.dtype)
    expenses = np.append(expenses, new_expense)

def update_expense(index, date=None, category=None, description=None, amount=None):
    if 0 <= index < len(expenses):
        if date:
            expenses[index]['date'] = date
        if category:
            expenses[index]['category'] = category
        if description:
            expenses[index]['description'] = description
        if amount:
            expenses[index]['amount'] = amount

def delete_expense(index):
    global expenses
    if 0 <= index < len(expenses):
        expenses = np.delete(expenses, index)

def view_expenses():
    for i, expense in enumerate(expenses):
        print(f"{i}: Date: {expense['date']}, Category: {expense['category']}, Description: {expense['description']}, Amount: {expense['amount']}")

def calculate_total_expense():
    return np.sum(expenses['amount'])

def calculate_expense_by_category(category):
    return np.sum(expenses[expenses['category'] == category]['amount'])

def calculate_average_expense():
    return np.mean(expenses['amount']) if len(expenses) > 0 else 0

def plot_expenses_by_category():
    categories = np.unique(expenses['category'])
    amounts = [calculate_expense_by_category(category) for category in categories]
    plt.bar(categories, amounts)
    plt.xlabel('Category')
    plt.ylabel('Total Expense')
    plt.title('Expenses by Category')
    plt.show()

def plot_expenses_over_time():
    dates = np.unique(expenses['date'])
    amounts = [np.sum(expenses[expenses['date'] == date]['amount']) for date in dates]
    plt.plot(dates, amounts, marker='o')
    plt.xlabel('Date')
    plt.ylabel('Total Expense')
    plt.title('Expenses Over Time')
    plt.xticks(rotation=45)
    plt.show()

def plot_expense_distribution():
    categories = np.unique(expenses['category'])
    amounts = [calculate_expense_by_category(category) for category in categories]
    plt.pie(amounts, labels=categories, autopct='%1.1f%%')
    plt.title('Expense Distribution by Category')
    plt.show()

def main_menu():
    while True:
        print("\nExpense Manager")
        print("1. Add Expense")
        print("2. Delete Expense")
        print("3. View Expenses")
        print("4. Calculate Total Expense")
        print("5. Calculate Expense by Category")
        print("6. Calculate Average Expense")
        print("7. Plot Expenses by Category")
        print("8. Plot Expenses Over Time")
        print("9. Plot Expense Distribution")
        print("10. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            add_expense(date, category, description, amount)
        elif choice == '2':
            index = int(input("Enter the index of the expense to delete: "))
            delete_expense(index)
        elif choice == '3':
            view_expenses()
        elif choice == '4':
            print("Total Expense:", calculate_total_expense())
        elif choice == '5':
            category = input("Enter category: ")
            print(f"Total Expense for {category}:", calculate_expense_by_category(category))
        elif choice == '6':
            print("Average Expense:", calculate_average_expense())
        elif choice == '7':
            plot_expenses_by_category()
        elif choice == '8':
            plot_expenses_over_time()
        elif choice == '9':
            plot_expense_distribution()
        elif choice == '10':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

