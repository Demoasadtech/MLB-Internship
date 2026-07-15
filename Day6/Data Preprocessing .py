'''Using the student_performance.csv dataset: (already provided with you)

Data Preprocessing

Load the dataset.
Encode any categorical columns if required.
Create a new column named Average_Score (if not already created).
Select appropriate feature columns (X) and target column (y).
Split the dataset into Training (80%) and Testing (20%).
Apply feature scaling where appropriate.'''

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd 
df=pd.read_csv("Day6/dirty_student_records.csv")
print(df.columns.to_list())
df.columns=df.columns.str.strip()
print("After spacing removed", df.columns)
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.dtypes)
columns = [
    "Machine Learning",
    "Robotics_desgin",
    "Digital_Electronics",
    "FeedbackControl",
    "Computer_Architecture"
]
df[columns] = df[columns].apply(pd.to_numeric, errors="coerce") # Convert columns to float type
print(df.dtypes)
for col in columns:
    df.loc[(df[col] < 0) | (df[col] > 100), col] = None
df[columns] = df[columns].fillna(df[columns].mean().round(2)) # Fill missing values with mean
df.rename(columns={'FeedbackControl': 'Feedback_Control_System', 'Robotics_desgin': 'Robotics_design'}, inplace=True)  # Rename column
print("Columns after renaming:", df.columns)
df['Average_Score'] = df[['Machine Learning', 'Robotics_design', 'Digital_Electronics','Feedback_Control_System','Computer_Architecture']].mean(axis=1).round(2)  # Calculate Average_Score
print(df)
df.drop(["Rank","Roll_No","Name","Total_marks"],axis=1, inplace=True)
print(df)
x_features=df.drop(["Average_Score"],axis=1)
y_prediction=df["Average_Score"]
X_train, X_test, y_train, y_test = train_test_split(
    x_features,
    y_prediction,
    test_size=0.2,
    random_state=42
)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print("Training Features Shape:", X_train.shape)
print("Testing Features Shape:", X_test.shape)
print("Training Target Shape:", y_train.shape)
print("Testing Target Shape:", y_test.shape)

