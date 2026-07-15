'''Student Score Prediction System

Build a simple Machine Learning application that:

Loads the dataset.
Preprocesses the data.
Trains a Linear Regression model.
Predicts student average scores.
Displays the model evaluation metrics.
Prints a comparison table of Actual vs Predicted scores.

Also Visualize the prediction results using a scatter plot showing Actual vs Predicted values.'''

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns
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
model=LinearRegression()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
print("Predicted Values:")
print(y_pred)
print("\nActual Values:")
print(y_test.values)
mbv=mean_absolute_error(y_test,y_pred)
print("Mean_absolute_value:",mbv)
msv=mean_squared_error(y_test,y_pred)
print("Mean_squared_value:",msv)
r2=r2_score(y_test,y_pred)
print("R2 scroe value:",r2)


plt.figure(figsize=(10,6))
plt.scatter(y_test, y_pred)
plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    color="red",
    linestyle="--"
)
plt.title("Actual vs Predicted Values")
plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")

plt.grid(True)
plt.savefig("Day6/actual_vs_predicted.png")
plt.show()

