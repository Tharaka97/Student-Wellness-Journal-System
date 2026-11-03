
from student_management import (
    get_valid_number,
    register_student,
    view_students,
    select_student,
    update_student
)


def display_menu():
    print("\n------ STUDENT WELLNESS JOURNAL--------")
    print("1. Register Student")
    print("2. View Students")
    print("3. Select Student")
    print("4. Update Student Details")
    print("5. Add Weekly Wellness Record")
    print("6. View and Search Wellness Records")
    print("7. View Wellness Summary")
    print("8. Exit")


def main():

    students = {}
    selected_student_id = None

    while True:

        display_menu()

        choice = get_valid_number(
            "Enter your choice: ", 1, 8, False
        )

        if choice == 1:
            selected_student_id = register_student(students)

        elif choice == 2:
            view_students(students)

        elif choice == 3:
            student_id = select_student(students)

            if student_id is not None:
                selected_student_id = student_id

        elif choice == 4:
            update_student(students)

        elif choice == 5:
            if selected_student_id is None:
                print("Please register or select a student first.")
            else:
                print("Weekly record module will be connected here.")

        elif choice == 6:
            if selected_student_id is None:
                print("Please select a student first.")
            else:
                print("Record viewing module will be connected here.")

        elif choice == 7:
            if selected_student_id is None:
                print("Please select a student first.")
            else:
                print("Wellness reporting module will be connected here.")

        elif choice == 8:
            print("Thank you for using Student Wellness Journal!")
            break


if __name__ == "__main__":
    main()
