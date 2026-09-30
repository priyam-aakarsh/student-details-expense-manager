from student_manager import student
from expense_manager import expenses

def show_report(year_only=False):
    total=sum(e["amount"] for e in expenses)
    if year_only:
        print("\n===== WHOLE YEAR EXPENSE REPORT =====")
        print("Student:",student["name"] or "Not added")
        print("Total Expense:",total)
        print("Number of Entries:",len(expenses))
        return

    print("\n===== COMPLETE REPORT =====")
    print("Name:",student["name"] or "Not added")
    print("Roll No:",student["roll_no"] or "Not added")
    print("Branch:",student["branch"] or "Not added")
    print("Semester:",student["semester"] or "Not added")
    print("Total Expense:",total)

    categories={}
    for e in expenses:
        categories[e["category"]]=categories.get(e["category"],0)+e["amount"]
    print("\nCategory-wise Expense:")
    for category,amount in categories.items():
        print(category,":",amount)
