'''Data Cleaning

Using the student_performance.csv dataset:

Check for missing values.
Remove duplicate records (if any).
Rename one or more columns.
Create a new column named Average_Score by calculating the average marks across all subjects.
Create another column named Performance using the following criteria:


Excellent → Average Score ≥ 90
Good → Average Score between 80 and 89
Average → Average Score between 70 and 79
Needs Improvement → Average Score below 70
Save the cleaned dataset as cleaned_student_performance.csv.'''

import pandas as pd
df=pd.read_csv("Day5/dirty_student_records.csv")
print(df.columns.tolist())
df.columns = df.columns.str.strip()  # Remove leading and trailing spaces from column names
print("Columns after stripping spaces:", df.columns)
print("Missing values in each column:")
print(df.isnull().sum())  # Check for missing values
print("Duplicate records:")
print(df.duplicated().sum())  # Check for duplicate records
df["Roll_No"]=df["Roll_No"].fillna("Unknown") # Fill missing Roll_No with mode
df["Name"]=df["Name"].fillna("Unknown") # Fill missing Name with mode
print(df.dtypes)
columns = [
    "Machine Learning",
    "Robotics_desgin",
    "Digital_Electronics",
    "FeedbackControl",
    "Computer_Architecture",
    "Total_marks"
]
columns_totalmarks = [
    "Machine Learning",
    "Robotics_desgin",
    "Digital_Electronics",
    "FeedbackControl",
    "Computer_Architecture"
]

df[columns] = df[columns].apply(pd.to_numeric, errors="coerce") # Convert columns to float type
print(df.dtypes)
df[columns] = df[columns].fillna(df[columns].mean().round(2)) # Fill missing values with mean
df["Total_marks"] = df[columns_totalmarks].sum(axis=1).round(2) # Calculate Total_marks
print(df["Total_marks"])
print("Missing values after filling Roll_No:", df.isnull().sum())
print("Renaming columns...")
print("Columns before renaming:", df.columns)
df.rename(columns={'FeedbackControl': 'Feedback_Control_System', 'Robotics_desgin': 'Robotics_design'}, inplace=True)  # Rename column
print("Columns after renaming:", df.columns)
print("Calculating Average Score...")
df['Average_Score'] = df[['Machine Learning', 'Robotics_design', 'Digital_Electronics','Feedback_Control_System','Computer_Architecture']].mean(axis=1).round(2)  # Calculate Average_Score
print(df)
df["Performance"] = df["Average_Score"].apply(
    lambda x: "Excellent" if x >= 90
    else "Good" if x >= 80
    else "Average" if x >= 70
    else "Needs Improvement"
)
df.to_csv("Day5/cleaned_student_performance.csv", index=False)  # Save cleaned dataset