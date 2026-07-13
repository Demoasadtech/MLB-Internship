'''Pandas

Using any sample CSV dataset (Students, Sales, or Titanic):

Load the dataset.
Display the first and last five rows.
Display dataset information.
Find missing values.
Filter data based on a condition.
Calculate summary statistics.'''

import pandas as pd
df = pd.read_csv('Day4/student_records.csv')
print(df.head())  # Display first five rows
print(df.tail())  # Display last five rows
print(df.info())  # Display dataset information
print(df.isnull().sum())  # Find missing values
print(df[df['Total_Marks'] > 300])  # Filter data based on a condition
print(df.describe())  # Calculate summary statistics
