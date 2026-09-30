from student_manager import student_menu
from expense_manager import expense_menu
from report_manager import show_report

while True:
    print("\n===== STUDENT DETAILS & EXPENSE MANAGER =====")
    print("1. Student Details")
    print("2. Daily Expenses")
    print("3. Whole Year Expenses")
    print("4. Complete Report")
    print("5. Exit")
    choice=input("Enter your choice: ")

    if choice=="1": student_menu()
    elif choice=="2": expense_menu()
    elif choice=="3": show_report(True)
    elif choice=="4": show_report(False)
    elif choice=="5":
        print("Thank you!")
        break
    else: print("Invalid choice.")
