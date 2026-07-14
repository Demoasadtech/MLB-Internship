
'''Data Visualization

Create the following charts:

Bar chart showing the average marks of each student.
Histogram showing the distribution of Average Scores.
Scatter plot comparing Python and Machine Learning marks.
Pie chart showing the distribution of students by Performance category.
Box plot to visualize the spread of marks in all subjects.'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("Day5/cleaned_student_performance.csv")
plt.figure(figsize=(20,6))
sns.set_theme(style="whitegrid")
sns.barplot(x="Name", y="Average_Score", data=df)
plt.xticks(rotation=90)
plt.title("Average Marks of Each Student")
plt.show()

plt.figure(figsize=(10,6))
sns.histplot(df['Average_Score'], bins=10, kde=True)
plt.title("Distribution of Average Scores")
plt.xlabel("Average Score")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(10,6))
sns.scatterplot(x="Robotics_design", y="Machine Learning", data=df)
plt.title("Robotics Design vs Machine Learning Marks")
plt.xlabel("Robotics Design Marks")
plt.ylabel("Machine Learning Marks")
plt.show()

plt.figure(figsize=(8,8))
performance_counts = df['Performance'].value_counts()
plt.pie(performance_counts, labels=performance_counts.index, autopct='%1.1f%%', startangle=90)
plt.title("Distribution of Students by Performance Category")
plt.show()


plt.figure(figsize=(10,6))
sns.boxplot(data=df[[ 'Machine Learning', 'Robotics_design', 'Digital_Electronics','Feedback_Control_System','Computer_Architecture']])
plt.title("Spread of Marks in All Subjects")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.xticks(rotation=45)
plt.show()
