
def get_valid_number(prompt, minimum, maximum, allow_decimal=True):

    while True:
        value = input(prompt).strip()

        if allow_decimal:
            valid_format = value.replace(".", "", 1).isdigit()
        else:
            valid_format = value.isdigit()

        if valid_format:
            number = float(value)

            if minimum <= number <= maximum:
                if allow_decimal:
                    return number
                else:
                    return int(number)

        print("Invalid input. Enter a number between",
              minimum, "and", maximum)


def get_valid_sex():
    while True:
        sex = input("Enter sex (Male/Female): ").strip().title()

        if sex == "Male" or sex == "Female":
            return sex
        else:
           print("Invalid input. Please enter Male or Female.")


def get_valid_mobile():
    while True:
        mobile = input("Enter mobile (Ex: +61424711962): ").strip()

        if (len(mobile) == 12
                and mobile.startswith("+614")
                and mobile[4:].isdigit()):
            return mobile
        else:

         print("Invalid mobile number. Use +614XXXXXXXX.")


def register_student(students):

    print("\n--------STUDENT REGISTRATION-----------")

    name = input("Enter student name: ").strip()

    while name == "":
        print("Name cannot be empty.")
        name = input("Enter student name: ").strip()

    age = get_valid_number("Enter age: ", 1, 120, False)
    sex = get_valid_sex()
    height = get_valid_number("Enter height (cm): ", 50, 250)
    weight = get_valid_number("Enter weight (kg): ", 1, 500)
    mobile = get_valid_mobile()

    student_id = "S" + str(len(students) + 1).zfill(3)

    while student_id in students:
        student_id = "S" + str(int(student_id[1:]) + 1).zfill(3)

    students[student_id] = {
        "name": name,
        "age": age,
        "sex": sex,
        "height": height,
        "weight": weight,
        "mobile": mobile,
        "weekly_records": {}
    }

    print("\nStudent registered successfully!")
    print("Student ID:", student_id)

    return student_id


def view_students(students):

    if len(students) == 0:
        print("\nNo students registered.")
        return

    print("\n------REGISTERED STUDENTS-------")

    for student_id, details in students.items():
        print("Student ID:", student_id)
        print("Name:", details["name"])
        print("Age:", details["age"])
        print("--------------------------")

        
def select_student(students):

    if len(students) == 0:
        print("\nNo students registered.")
        return None

    view_students(students)

    student_id = input("Enter Student ID: ").strip().upper()

    if student_id in students:
        print("Selected student:", students[student_id]["name"])
        return student_id

    print("Student ID not found!")
    return None


def update_student(students):

    student_id = select_student(students)

    if student_id is None:
        return

    print("\n-------UPDATE STUDENT DETAILS -------")

    print("1. Update Name")
    print("2. Update Age")
    print("3. Update Height")
    print("4. Update Weight")
    print("5. Update Mobile")
    print("6. Cancel")

    choice = get_valid_number("Enter choice: ", 1, 6, False)

    if choice == 1:
        name = input("Enter new name: ").strip()

        while name == "":
            name = input("Name cannot be empty. Enter new name: ").strip()

        students[student_id]["name"] = name

    elif choice == 2:
        students[student_id]["age"] = get_valid_number(
            "Enter new age: ", 1, 120, False
        )

    elif choice == 3:
        students[student_id]["height"] = get_valid_number(
            "Enter new height: ", 50, 250
        )

    elif choice == 4:
        students[student_id]["weight"] = get_valid_number(
            "Enter new weight: ", 1, 500
        )

    elif choice == 5:
        students[student_id]["mobile"] = get_valid_mobile()

    else:
        return

