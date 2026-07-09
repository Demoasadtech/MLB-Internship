Students=[]  # Empty list to store student records

#add_ student() function is used to add student records

def add_student():

    
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

    print("Student added successfully!")

#display_students() function is used to display all student records

def display_students():
    if not Students:
        print("No student records found.")
        return
    print("Student Records:")
    for student in Students:
        print(f"Name: {student['name']}, Roll No: {student['roll_no']}, Age: {student['age']}, Course: {student['course']}")

#search_student() function is used to search student records by roll number

def search_student():
    roll_no=int(input("Enter student Roll No to search: "))
    for student in Students:
        if student['roll_no']==roll_no:
            print(f"Student found: Name: {student['name']}, Roll No: {student['roll_no']}, Age: {student['age']}, Course: {student['course']}")
            return
    print("Student not found.")  

#update_student_information() function is used to update student records by roll number

def update_student_information():
    roll_no=int(input("Enter student Roll No to update: "))
    for student in Students:
        if student['roll_no']==roll_no:
            Student_name=input("Enter new student name: ")
            Student_age=input("Enter new student age: ")
            Student_course=input("Enter new student course: ")
            student['name']=Student_name
            student['age']=Student_age
            student['course']=Student_course
            print("Student record updated successfully!")
            return
    print("Student not found.") 

#delete_student() function is used to delete student records by roll number

def delete_student():
    roll_no=int(input("Enter student Roll No to delete: "))
    for student in Students:
        if student['roll_no']==roll_no:
            Students.remove(student)
            print("Student record deleted successfully!")
            return
    print("Student not found.")

def display_total_students():
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
              