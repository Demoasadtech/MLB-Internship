'''Student Performance Dashboard

Using the dataset, create a simple analysis notebook or Python script that answers the following questions:

How many students are in the dataset?
What is the average score for each subject?
Who are the Top 5 performing students?
Which students need improvement?
Which subject has the highest class average?
Visualize your findings using appropriate charts.'''
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
os.makedirs("Day5/generated_charts", exist_ok=True)

df = pd.read_csv("Day5/cleaned_student_performance.csv")
print("Number of students in the dataset:", len(df)) # 1. How many students are in the dataset?
print(df[["Name","Average_Score"]])   # print average_score of each students

plt.figure(figsize=(20,6))
sns.set_theme(style="whitegrid")       # for Visualization using barplot
sns.barplot(x="Name", y="Average_Score", data=df)
plt.xticks(rotation=90)
plt.title("Average Marks of Each Student")
plt.show()

top5=df.sort_values(by="Average_Score", ascending=False).head(5)  # find top5 students
top5_students=top5[["Name","Average_Score"]]
print(top5_students)

plt.figure(figsize=(20,6))  #for visualization top5 students
sns.barplot(
    x="Name",
    y="Average_Score",
    data=top5
)
plt.title("Top 5 Performing Students")
plt.savefig("Day5/generated_charts/Top 5 Performing Students.png", dpi=300)
plt.show()

need = df[df["Performance"]=="Needs Improvement"] # Students who need improvement
print(need[["Name","Average_Score"]])

plt.figure(figsize=(20,6))  # for visulaization 
sns.barplot(
    x="Name",
    y="Average_Score",
    data=need
)
plt.title("Students Who Need Improvement")
plt.xticks(rotation=90)
plt.savefig("Day5/generated_charts/Students Who Need Improvement.png", dpi=300)
plt.show()

subjects = [
    "Machine Learning",
    "Robotics_design",
    "Digital_Electronics",
    "Feedback_Control_System",
    "Computer_Architecture"
]
subject_average=df[subjects].mean()    # find highest avrage subject
print("Highest Average Subject :", subject_average.idxmax())


plt.figure(figsize=(20,6)) #for visualization 
sns.barplot(
    x=subject_average.index,
    y=subject_average.values
)
plt.title("Class Average by Subject")
plt.xticks(rotation=45)
plt.savefig("Day5/generated_charts/Class Average by Subject", dpi=300)
plt.show()


performance = df["Performance"].value_counts()   # piechart visualization  for student performance distribution
plt.figure(figsize=(20,6))
plt.pie(
    performance,
    labels=performance.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Student Performance Distribution")
plt.savefig("DAY5/generated_charts/Student Performance Distribution", dpi=300)
plt.show()

plt.figure(figsize=(20,6))    # histrogram visulaization for distribution fo average score
sns.histplot(
    df["Average_Score"],
    bins=10,
    kde=True
)
plt.title("Distribution of Average Scores")
plt.savefig("Day5/generated_charts/Distribution of Average Scores", dpi=300)
plt.show()



plt.figure(figsize=(10,6))   #boxplot visualization for find spread marks in all subjects
sns.boxplot(data=df[subjects])
plt.title("Spread of Marks in All Subjects")
plt.xticks(rotation=45)
plt.savefig("Day5/generated_charts/Spread of Marks in All Subjects", dpi=300)
plt.show()