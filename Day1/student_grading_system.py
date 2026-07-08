print("========== Student Grading System ==========\n")

student_name = input("Enter Student Name: ")
student_class = input("Enter Class: ")

num_subjects = int(input("Enter Number of Subjects: "))

subjects = []
marks = []
total = 0

for i in range(num_subjects):
    subject = input(f"\nEnter Subject {i+1} Name: ")
    mark = float(input(f"Enter Marks in {subject}: "))

    subjects.append(subject)
    marks.append(mark)
    total += mark

average = total / num_subjects

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "F"

print("\n========== RESULT ==========")
print("Student Name :", student_name)
print("Class        :", student_class)

print("\nSubjects and Marks:")
for i in range(num_subjects):
    print(f"{subjects[i]} : {marks[i]}")

print("\nTotal Marks :", total)
print("Average     :", round(average, 2))
print("Grade       :", grade)