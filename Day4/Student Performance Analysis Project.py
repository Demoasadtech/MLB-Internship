
'''Student Performance Analysis

Using a CSV dataset containing student records, perform the following:

Load the dataset using Pandas.
Display basic information about the dataset.
Calculate average marks for each subject.
Identify the top 5 performing students.
Find students scoring below the average.
Display the total number of students.
Save the cleaned or analyzed dataset as a new CSV file.'''

import numpy as np
import pandas as pd
df = pd.read_csv('Day4/student_records.csv')
# Display basic information about the dataset
print(df.head())  # Display first five rows
print(df.tail())  # Display last five rows
print(df.info())  # Display dataset information
print(df.isnull().sum())  # Find missing values
print(df.describe())  # Calculate summary statistics
# Calculate average marks for each subject
print("Average marks for each subject:")
average_marks = df[['Machine_Learning', 'Robotics_Design', 'Digital_Electronics', 'Feedback_Control', 'Computer_Architecture']].mean()  #Average marks for each subject
print(average_marks)
print ("Top 5 performing students:")
# Identify the top 5 performing students based on Total_Marks
top_students = df.nlargest(5, 'Total_Marks')  # Top 5 performing students
print(top_students)
# Find students scoring below the average in Total_Marks
average_total_marks = df['Total_Marks'].mean()  # Average Total_Marks
print("Average Total_Marks:", average_total_marks)
print("Students scoring below the average Total_Marks:")
below_average_students = df[df['Total_Marks'] < average_total_marks]
print(below_average_students)
print("Total number of students:", len(df))  # Display the total number of students
# Save the cleaned or analyzed dataset as a new CSV file
df.to_csv('Day4/analyzed_student_records.csv', index=False)  # Save the analyzed dataset as a new CSV file