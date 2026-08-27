expenses = []


def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }

    expenses.append(expense)

    print("\nExpense added successfully!")


def view_expenses():
    if len(expenses) == 0:
        print("\nNo expenses found.")
        return

    print("\n========== ALL EXPENSES ==========")

    for i, expense in enumerate(expenses, start=1):
        print("Expense No.:", i)
        print("Date:", expense["date"])
        print("Category:", expense["category"])
        print("Amount: Rs.", expense["amount"])
        print("Description:", expense["description"])
        print("----------------------------------")


def total_expense():
    if len(expenses) == 0:
        print("\nNo expenses found.")
        return

    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print("\nTotal Expense: Rs.", total)


def highest_expense():
    if len(expenses) == 0:
        print("\nNo expenses found.")
        return

    highest = expenses[0]

    for expense in expenses:
        if expense["amount"] > highest["amount"]:
            highest = expense

    print("\n========== HIGHEST EXPENSE ==========")
    print("Category:", highest["category"])
    print("Amount: Rs.", highest["amount"])
    print("Description:", highest["description"])


def search_category():
    category = input("Enter category to search: ")

    found = False

    print("\n========== SEARCH RESULT ==========")

    for expense in expenses:
        if expense["category"].lower() == category.lower():
            print("Date:", expense["date"])
            print("Category:", expense["category"])
            print("Amount: Rs.", expense["amount"])
            print("Description:", expense["description"])
            print("----------------------------------")
            found = True

    if found == False:
        print("No expenses found in this category.")


def expense_count():
    print("\nNumber of expenses:", len(expenses))


while True:

    print("\n====================================")
    print("       STUDENT EXPENSE TRACKER")
    print("====================================")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Calculate Total Expense")
    print("4. Find Highest Expense")
    print("5. Search by Category")
    print("6. Count Expenses")
    print("7. Exit")
    print("====================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        highest_expense()

    elif choice == "5":
        search_category()

    elif choice == "6":
        expense_count()

    elif choice == "7":
        print("\nThank you for using Student Expense Tracker!")
        break

    else:
        print("\nInvalid choice! Please enter a number from 1 to 7.")

