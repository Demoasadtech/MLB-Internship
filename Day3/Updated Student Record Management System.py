import os
import json

def load_students():  #load_students() function is used to load student records from the JSON file
    if os.path.exists("Day3/Student Records Management System.json"):
        try:
            with open("Day3/Student Records Management System.json", "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    return []


def save_students(students): #save_students() function is used to save student records to the JSON file
    try:
        with open("Day3/Student Records Management System.json", "w") as file:
            json.dump(students, file, indent=4)
    except PermissionError:
        print("You don't have permission to write to this file.")
    except Exception as e:
        print("Unexpected Error:", e)

def add_student():    
    Students = load_students()  # Load student records from the JSON file
    while True:
        Student_name = input("Enter Name: ").strip()

        if Student_name == "":
            print("Name cannot be empty!")
        else:
            break


    while True:
        Student_roll = input("Enter Roll Number: ").strip()

        if Student_roll == "":
            print("Roll Number cannot be empty!")
            continue

        duplicate = False

        for student in Students:
            if student["roll_no"] == Student_roll:
                duplicate = True
                break

        if duplicate:
            print("Roll Number already exists!")
        else:
            break

    while True:
        Student_age = input("Enter Age: ").strip()

        if Student_age.isdigit() and int(Student_age) > 0:
            Student_age = int(Student_age)
            break
        else:
            print("Enter a valid age!")

   
    while True:
        Student_course = input("Enter Course: ").strip()

        if Student_course == "":
            print("Course cannot be empty!")
        else:
            break

    student = {
        "name": Student_name,
        "roll_no": Student_roll,
        "age": Student_age,
        "course": Student_course
    }

    Students.append(student)
    save_students(Students)  # Save the updated student records to the JSON file
    print("Student added successfully!")
  
def display_students():
    Students = load_students()  # Load student records from the JSON file
    if not Students:
        print("No student records found.")
        return
    else:
        print("Student Records:")
        for student in Students:
            print("-" * 35)
            print(f"Name     : {student['name']}")
            print(f"Roll No  : {student['roll_no']}")
            print(f"Age      : {student['age']}")
            print(f"Course   : {student['course']}")

def search_student():  #search_student() function is used to search student records by roll number
    Students = load_students()  # Load student records from the JSON file
    roll_no=input("Enter student Roll No to search: ").strip()
    for student in Students:
        if student['roll_no']==roll_no:
            print("-" * 35)
            print(f"Name     : {student['name']}")
            print(f"Roll No  : {student['roll_no']}")
            print(f"Age      : {student['age']}")
            print(f"Course   : {student['course']}")             
            return
    print("Student not found.")  

#update_student_information() function is used to update student records by roll number

def update_student_information():
    students = load_students()

    roll_no = input("Enter Roll Number to update: ").strip()

    for student in students:

        if student["roll_no"] == roll_no:

            while True:
                name = input("Enter New Name: ").strip()
                if name == "":
                    print("Name cannot be empty!")
                else:
                    break

            while True:
                age = input("Enter New Age: ").strip()
                if age.isdigit() and int(age) > 0:
                    age = int(age)
                    break
                else:
                    print("Enter valid age!")

            while True:
                course = input("Enter New Course: ").strip()
                if course == "":
                    print("Course cannot be empty!")
                else:
                    break

            student["name"] = name
            student["age"] = age
            student["course"] = course

            save_students(students)

            print("Student record updated successfully!")
            return

    print("Student not found.")

#delete_student() function is used to delete student records by roll number

def delete_student():
    Students = load_students()  # Load student records from the JSON file
    roll_no=input("Enter student Roll No to delete: ").strip()
    for student in Students:
        if student['roll_no']==roll_no:
            Students.remove(student)
            save_students(Students)  # Save the updated student records to the JSON file
            print("Student record deleted successfully!")
            return
    print("Student not found.")

def display_total_students():
    Students = load_students()  # Load student records from the JSON file
    print(f"Total number of students: {len(Students)}")

#main program loop

while True:

    print("====== Student Record Management System ======")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Display Total Students")
    print("7. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student_information()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        display_total_students()

    elif choice == "7":
        print("Program Closed.")
        break

    else:
        print("Invalid Choice")
              