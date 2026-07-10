#===================Practice Problems===================
import os
import json

#File Handling

#Create a text file and write data into it.
#Read and display file contents.
#Append new data to an existing file.
#Count the number of lines in a file.

with open("Day3/input.txt", "w") as file:    #Create a text file and write data into it.
    file.write("Hello World\n")
    file.write("My name is Asad.\n")
    file.write("Practice problems are fun!\n")
    print("Data written to file successfully.")

with open("Day3/input.txt", "r") as file:   #Read and display file contents.
    data1 = file.read()
with open("Day3/input.txt", "r") as file:
    data2 = file.readlines()
    print(data1)
    print(data2)

with open("Day3/input.txt", "a") as file:  #Append new data to an existing file.
    file.write("Appending new data.\n")
    print("Data appended to file successfully.")

with open("Day3/input.txt", "r") as file:  #Count the number of lines in a file.
    count = 0
    for line in file:
        count += 1
    print("Number of lines in the file:", count)



#JSON

#Store student information in a JSON file.
#Read data from a JSON file.
#Update an existing student's information.
#Add a new student to the JSON file.

with open("Day3/students.json", "w") as file:  #Store student information in a JSON file.
    students = [
        {"name": "Asad", "age": 20, "grade": "A"},
        {"name": "Ali", "age": 21, "grade": "B"},
        {"name": "Sara", "age": 19, "grade": "A"}
    ]
    json.dump(students, file , indent=4)
    print("Student information stored in JSON file successfully.")

with open("Day3/students.json", "r") as file:  #Read data from a JSON file.
    data = json.load(file)
    print("Data read from JSON file:")
    print(data)


with open("Day3/students.json", "r+") as file:  #Update an existing student's information.

    data = json.load(file)

    name_student = input("Enter the name of the student to update: ")

    found = False

    for student in data:
        if student["name"] == name_student:
            student["grade"] = input("Enter the new grade: ")
            found = True
            break

    if found:
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()
        print("Student information updated successfully.")
    else:
        print("Student not found.")

with open("Day3/students.json", "r+") as file:  #Add a new student to the JSON file.
    data1 = json.load(file)
    new_student = {
        "name": input("Enter the name of the new student: "),
        "age": int(input("Enter the age of the new student: ")),
        "grade": input("Enter the grade of the new student: ")
    }
    data1.append(new_student)
    file.seek(0)
    json.dump(data1, file, indent=4)
    file.truncate()
    print("New student added to JSON file successfully.")
