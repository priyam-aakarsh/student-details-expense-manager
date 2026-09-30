student={"name":"","roll_no":"","branch":"","semester":"","phone":"","email":""}

def student_menu():
    while True:
        print("\n--- STUDENT DETAILS ---")
        print("1. Add / Update Details")
        print("2. View Details")
        print("3. Back")
        choice=input("Enter choice: ")

        if choice=="1":
            student["name"]=input("Enter name: ")
            student["roll_no"]=input("Enter roll number: ")
            student["branch"]=input("Enter branch: ")
            student["semester"]=input("Enter semester: ")
            student["phone"]=input("Enter phone: ")
            student["email"]=input("Enter email: ")
            print("Details saved.")
        elif choice=="2":
            for key,value in student.items():
                print(key.replace("_"," ").title()+":", value if value else "Not added")
        elif choice=="3": break
        else: print("Invalid choice.")
