# Day 3 - File Handling & JSON in Python

## 📌 Overview

Today I learned File Handling and JSON in Python. I practiced reading, writing, updating, and storing data permanently using text files and JSON files. I also upgraded my Student Record Management System with persistent data storage and exception handling.

---

## 🔗 How File Handling and JSON Work Together

File Handling allows Python programs to create, read, write, and update files, while JSON provides a structured format for storing data. In this project, File Handling was used to open and manage the JSON file, and the JSON module was used to convert Python dictionaries and lists into JSON format and back into Python objects. Together, they allowed the Student Record Management System to save and retrieve student records permanently.

---

## ⚡ Challenges Faced

During this project, I faced several challenges:

- Understanding how to make the Student Record Management System persistent by storing data permanently in a JSON file.
- Building the program logic for loading existing data when the application starts and saving updated records after every operation.
- Initially, I tried to build the complete logic on my own, but the code became lengthy, difficult to understand, and did not work correctly.
- I found it challenging to organize the code in a clean and reusable way, as similar code was being repeated in multiple functions.
- Managing file handling and JSON operations together was confusing at first, especially when updating and saving records.
- To improve my understanding and logic-building skills, I took guidance from ChatGPT.
- Based on that guidance, I created two reusable functions: `load_students()` and `save_students()`.
- Instead of repeating the same code, I simply called these functions whenever data needed to be loaded or saved.
- This made my code cleaner, more efficient, easier to maintain, more memory-efficient, and closer to professional coding practices.

These challenges helped me improve my understanding of file handling, JSON, code reusability, and writing cleaner and more structured Python programs.

---

# 📚 Topics Covered

## File Handling in Python

- Opening and closing files
- Reading from text files
- Writing to text files
- Appending data to files
- Using the `with` statement
- File modes (`r`, `w`, `a`)

## JSON in Python

- What JSON is and why it's commonly used
- Reading JSON files
- Writing data to JSON files
- Converting Python dictionaries to JSON
- Loading JSON data into Python objects

---

# 💻 Coding Practice

## File Handling

- Created a text file and wrote data into it
- Read and displayed file contents
- Appended new data to an existing file
- Counted the number of lines in a file

## JSON

- Stored student information in a JSON file
- Read data from a JSON file
- Updated an existing student's information
- Added a new student to the JSON file

---

# 🚀 Today Task (MLB-Internship/Day3)

## Student Record Management System (Persistent Version)

### Features

- Save student records to a JSON file
- Load existing records automatically
- Add student records
- Search student records
- Update student records
- Delete student records
- Permanently save all changes
- Handle invalid inputs using exception handling

---

# 🛠️ Technologies Used

- Python 3
- File Handling
- JSON
- Exception Handling
- Functions
- Lists
- Dictionaries

---

# 📂 Project Structure

```
Day3/
│── input.txt
│── Practice_Problems.py
│── README.md
│── requirements.txt
│── Student Records Management System.py
│── students.json
│── Updated Student Record Management System.py
```

---

# 📖 Description of Files

| File | Description |
|------|-------------|
| `Practice_Problems.py` | Practice programs for File Handling and JSON concepts |
| `input.txt` | Text file used for File Handling practice |
| `students.json` | JSON file used to store student records |
| `Student Records Management System.json` | json file which stored data of the Student Record Management System |
| `Updated Student Record Management System.py` | Persistent version with JSON storage and exception handling |
| `requirements.txt` | Project dependencies |
| `README.md` | Project documentation |

---

# 🎯 Learning Outcomes

After completing Day 3, I learned how to:

- Work with text files using Python
- Read, write and append file data
- Use file modes (`r`, `w`, `a`)
- Store data permanently using JSON
- Read and update JSON files
- Convert Python dictionaries to JSON
- Load JSON data into Python objects
- Handle errors using Exception Handling (`try`, `except`)
- Build a persistent Student Record Management System

---

## 👨‍💻 Author

**Muhammad Asad Ali**
