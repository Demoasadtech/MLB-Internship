# Day 1 - ML Internship

## Topics Covered

- Python Fundamentals
- Virtual Environment
- Git & GitHub Basics

## Project Setup

### Step 1: Create Project Folder

Created a project folder named **MLB-Internship**.

### Step 2: Create Virtual Environment

Created a virtual environment using the following command:

```bash
python -m venv venv
```

Activated the virtual environment using:

```bash
venv\Scripts\activate
```

### Step 3: Project Structure

```
MLB-Internship/
│
├── .gitignore
├── Day1/
│   ├── student_grading_system.py
│   └── README.md
│
└── venv/
```

### Step 4: Git Initialization

Initialized Git repository:

```bash
git init
```

### Step 5: Student Grading System

Developed a Python program that:

- Takes student name as input.
- Takes class name as input.
- Takes the number of subjects.
- Takes subject names and marks.
- Calculates the average marks.
- Assigns grades based on the average.

### Grade Criteria

- **A** : 90 - 100
- **B** : 75 - 89
- **C** : 50 - 74
- **F** : Below 50

## Git Commands Used

```bash
git init
git add .
git commit -m "Day 1 ML Internship"
git branch -M main
git remote add origin https://github.com/Demoasadtech/MLB-Internship.git
git push -u origin main
```