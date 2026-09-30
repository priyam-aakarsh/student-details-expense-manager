expenses=[]

def add_expense():
    date=input("Enter date (DD-MM-YYYY): ")
    category=input("Enter category (Food/Travel/Study/Other): ")
    item=input("Enter item: ")
    try:
        amount=float(input("Enter amount: "))
        if amount<0:
            print("Amount cannot be negative.")
            return
        expenses.append({"date":date,"category":category,"item":item,"amount":amount})
        print("Expense added.")
    except ValueError:
        print("Enter a valid amount.")

def daily_expenses():
    date=input("Enter date: ")
    total=0
    found=False
    print("\n--- DAILY EXPENSES ---")
    for e in expenses:
        if e["date"]==date:
            print(e["category"], "-", e["item"], ":", e["amount"])
            total+=e["amount"]; found=True
    print("Total:",total) if found else print("No expense found.")

def all_expenses():
    total=0
    print("\n--- ALL / WHOLE YEAR EXPENSES ---")
    if not expenses:
        print("No expenses added."); return
    for e in expenses:
        print(e["date"],"|",e["category"],"|",e["item"],"|",e["amount"])
        total+=e["amount"]
    print("Total Expense:",total)

def expense_menu():
    while True:
        print("\n--- EXPENSE MANAGEMENT ---")
        print("1. Add Expense")
        print("2. View Daily Expenses")
        print("3. View Whole Year Expenses")
        print("4. Back")
        choice=input("Enter choice: ")
        if choice=="1": add_expense()
        elif choice=="2": daily_expenses()
        elif choice=="3": all_expenses()
        elif choice=="4": break
        else: print("Invalid choice.")
