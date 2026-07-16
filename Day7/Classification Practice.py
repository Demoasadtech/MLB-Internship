'''Coding Practice

Model Evaluation

Train a simple classification model.
Evaluate it using Accuracy, Precision, Recall, and F1-Score.
Generate a Confusion Matrix.
Understand what each metric tells you about the model.

Classification

Use a dataset such as:

Iris Dataset (Recommended)
Breast Cancer Dataset
Wine Dataset

Tasks:

Load the dataset. (from Scikit-learn built-in datasets)
Explore the features and target classes.
Split the data into training and testing sets.
Train a Logistic Regression model.
Make predictions.
Evaluate the model using the metrics above.'''

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score,accuracy_score,recall_score,f1_score,confusion_matrix,classification_report
iris=load_iris()
x_features=iris.data
y_values=iris.target
print(y_values)
df=pd.DataFrame(x_features,columns=iris.feature_names)
df["Species"] = [iris.target_names[i] for i in y_values]
X_train, X_test, y_train, y_test = train_test_split(
    x_features, y_values, test_size=0.2, random_state=42
)
model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

a_score=accuracy_score(y_test,y_pred)
print("Accuracy is : ",a_score)
p_score=precision_score(y_test,y_pred,average="weighted")
print("Precision is : ",p_score)
r_score=recall_score(y_test,y_pred,average="weighted")
print("Recall is : ",r_score)
f_score=f1_score(y_test,y_pred,average="weighted")
print("F1 Score is  : ",f_score)
C_report=classification_report(y_test,y_pred)
print("Classification_Report : ")
print(C_report)
cm=confusion_matrix(y_test,y_pred)
plt.figure(figsize=(6,5))
sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=iris.target_names,
    yticklabels=iris.target_names
)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()

