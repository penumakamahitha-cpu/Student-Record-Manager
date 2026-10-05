import re

FILE_NAME = "students.txt"


def add_student():
    try:
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")

        age = int(input("Enter Age: "))

        email = input("Enter Email: ")

        # Email validation using Regex
        pattern = r"^[\w.-]+@[\w.-]+\.\w+$"

        if not re.match(pattern, email):
            print("Invalid email address!")
            return

        with open(FILE_NAME, "a") as file:
            file.write(f"{student_id},{name},{age},{email}\n")

        print("Student added successfully!")

    except ValueError:
        print("Invalid input! Age must be a number.")

    except Exception as e:
        print("Error:", e)


def view_students():
    try:
        with open(FILE_NAME, "r") as file:
            students = file.readlines()

        if not students:
            print("No student records found.")
            return

        print("\n===== STUDENT RECORDS =====")

        for student in students:
            data = student.strip().split(",")

            print("ID:", data[0])
            print("Name:", data[1])
            print("Age:", data[2])
            print("Email:", data[3])
            print("---------------------------")

    except FileNotFoundError:
        print("No student records found.")


def main():
    while True:
        print("\n===== STUDENT RECORD MANAGER =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_student()

            elif choice == 2:
                view_students()

            elif choice == 3:
                print("Thank you!")
                break

            else:
                print("Please enter 1, 2, or 3.")

        except ValueError:
            print("Invalid input! Please enter a number.")


if __name__ == "__main__":
    main()
