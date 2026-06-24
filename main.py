def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    branch = input("Enter Branch: ")

    with open("students.txt", "a") as file:
        file.write(f"{roll},{name},{branch}\n")

    print("✅ Student record added successfully!")


def view_students():
    try:
        with open("students.txt", "r") as file:
            records = file.readlines()

            if not records:
                print("No records found.")
                return

            print("\n===== STUDENT RECORDS =====")

            for record in records:
                roll, name, branch = record.strip().split(",")
                print(f"Roll No: {roll} | Name: {name} | Branch: {branch}")

    except FileNotFoundError:
        print("No records found.")


def search_student():
    roll_to_search = input("Enter Roll Number to Search: ")

    try:
        with open("students.txt", "r") as file:
            found = False

            for record in file:
                roll, name, branch = record.strip().split(",")

                if roll == roll_to_search:
                    print("\n===== STUDENT FOUND =====")
                    print("Roll No:", roll)
                    print("Name:", name)
                    print("Branch:", branch)
                    found = True
                    break

            if not found:
                print("Student not found.")

    except FileNotFoundError:
        print("No records found.")


def update_student():
    roll_to_update = input("Enter Roll Number to Update: ")

    try:
        with open("students.txt", "r") as file:
            records = file.readlines()

        found = False

        with open("students.txt", "w") as file:
            for record in records:
                roll, name, branch = record.strip().split(",")

                if roll == roll_to_update:
                    print("\nEnter New Details")
                    new_name = input("Enter New Name: ")
                    new_branch = input("Enter New Branch: ")

                    file.write(f"{roll},{new_name},{new_branch}\n")
                    found = True
                else:
                    file.write(record)

        if found:
            print("✅ Student record updated successfully!")
        else:
            print("Student not found.")

    except FileNotFoundError:
        print("No records found.")


def delete_student():
    roll_to_delete = input("Enter Roll Number to Delete: ")

    try:
        with open("students.txt", "r") as file:
            records = file.readlines()

        found = False

        with open("students.txt", "w") as file:
            for record in records:
                roll, name, branch = record.strip().split(",")

                if roll != roll_to_delete:
                    file.write(record)
                else:
                    found = True

        if found:
            print("✅ Student record deleted successfully!")
        else:
            print("Student not found.")

    except FileNotFoundError:
        print("No records found.")


# Main Menu
while True:
    print("\n")
    print("====================================")
    print(" STUDENT RECORD MANAGEMENT SYSTEM")
    print("====================================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank you for using the system!")
        break

    else:
        print(" Invalid choice. Please enter a number between 1 and 6.")
