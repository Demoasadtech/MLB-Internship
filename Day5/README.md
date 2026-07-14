# Day 5 - Data Cleaning and Data Visualization

## 📌 Overview

In this project, I learned how to clean real-world data using **Pandas** and visualize insights using **Matplotlib** and **Seaborn**. I cleaned the student performance dataset, handled missing values, created new features, and generated meaningful charts to analyze student performance.

---

## 📂 Files Included

- `DataCleaning.py`
- `DataVisualization.py`
- `Student Performance Dashboard.py`
- `dirty_student_records.csv`
- `cleaned_student_performance.csv`
- `requirements.txt`
- `generated_charts/`
- `README.md`

---

# Data Cleaning

The following data cleaning steps were performed:

- Checked for missing values.
- Filled missing values:
  - Text columns (`Name`, `Roll_No`) with `"Unknown"`.
  - Subject marks with the column mean.
- Removed duplicate records.
- Renamed inconsistent column names.
- Converted subject columns to numeric data types.
- Updated the `Total_marks` column.
- Created a new `Average_Score` column.
- Created a `Performance` column based on average marks.
- Saved the cleaned dataset as `cleaned_student_performance.csv`.

---

# Data Visualization

The following visualizations were created:

1. **Bar Chart**
   - Average score of each student.

2. **Histogram**
   - Distribution of Average Scores.

3. **Scatter Plot**
   - Comparison between Machine Learning and Digital Electronics marks.

4. **Pie Chart**
   - Distribution of students by Performance category.

5. **Box Plot**
   - Spread of marks across all subjects.

6. **Dashboard Charts**
   - Subject-wise class average.
   - Top 5 performing students.
   - Students needing improvement.
   - Performance distribution.
   - Distribution of average scores.
   - Subject marks spread.

All charts were saved as PNG images inside the `generated_charts` folder.

---

# Mini Project

## Student Performance Dashboard

The dashboard answers the following questions:

- Total number of students in the dataset.
- Average score of each subject.
- Top 5 performing students.
- Students who need improvement.
- Subject with the highest class average.

---

# Key Insights

1. **Feedback_Control_System** achieved the highest class average among all subjects.
2. Most students fall into the **Good** and **Average** performance categories.
3. Only a small number of students require improvement, while a few students achieved Excellent performance.

---

# Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn

---

# Learning Outcomes

By completing this project, I learned how to:

- Clean real-world datasets using Pandas.
- Handle missing values and duplicate records.
- Rename columns and change data types.
- Create new calculated columns.
- Build meaningful visualizations using Matplotlib and Seaborn.
- Perform exploratory data analysis.
- Present findings in a clear and professional manner.

---

# Project Structure

```
Day5/
│
├── DataCleaning.py
├── DataVisualization.py
├── Student Performance Dashboard.py
├── dirty_student_records.csv
├── cleaned_student_performance.csv
├── requirements.txt
├── README.md
│
└── generated_charts/
    ├── Class Average by Subject.png
    ├── Distribution of Average Scores.png
    ├── Spread of Marks in All Subjects.png
    ├── Student Performance Distribution.png
    ├── Students Who Need Improvement.png
    └── Top 5 Performing Students.png
```

---

## Author

**Muhammad Asad Ali**
