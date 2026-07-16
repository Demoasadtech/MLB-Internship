'''Iris Flower Classification System

Build a classification system that predicts the species of an Iris flower based on its features.

The project should:

Load and explore the dataset.
Train a Logistic Regression model.
Predict flower species.
Display model evaluation metrics.
Show the Confusion Matrix.
Print sample predictions with actual values.

Bonus (Optional):

Train a Decision Tree model as well.
Compare its performance with Logistic Regression.'''
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
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
model_linear = LogisticRegression() # logistic regression model
model_linear.fit(X_train, y_train)
y_pred = model_linear.predict(X_test)
#print Sample prediction and actual values of logistic regression
print("Sample prediction and actual values of logistic regression ")
print("Atual values")
print(y_test)
print("Sample Prediction")
print(y_pred)
model_tree=DecisionTreeClassifier() # Decision Tree Classfier
model_tree.fit(X_train,y_train)
tree_pred=model_tree.predict(X_test)
#print Sample prediction and actual values of Decision Tree
print("Sample prediction and actual values of Decision Tree")
print("Atual values")
print(y_test)
print("Sample Prediction")
print(tree_pred)
#Evaluation & Confusion matric of logistic Regression
print(f'{"="*6} Evaluation & Confusion matric of logistic Regression{"="*6}')
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
#Evaluation & Confusion matric of Decision Tree
print(f'{"="*6} Evaluation & Confusion matric of Decision Tree{"="*6}')
a_score_t=accuracy_score(y_test,tree_pred)
print("Accuracy is : ",a_score_t)
p_score_t=precision_score(y_test,tree_pred,average="weighted")
print("Precision is : ",p_score_t)
r_score_t=recall_score(y_test,tree_pred,average="weighted")
print("Recall is : ",r_score_t)
f_score_t=f1_score(y_test,tree_pred,average="weighted")
print("F1 Score is  : ",f_score_t)
C_report_t=classification_report(y_test,tree_pred)
print("Classification_Report : ")
print(C_report_t)
L_g=confusion_matrix(y_test,y_pred)
D_t=confusion_matrix(y_test,tree_pred)
plt.subplot(1,2,1)
# Logistic regression heatmap
sns.heatmap(
    L_g,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=iris.target_names,
    yticklabels=iris.target_names
)

plt.title("Logistic Regression")
plt.xlabel("Predicted")
plt.ylabel("Actual")

# Decision Tree heatmap,
plt.subplot(1,2,2)

sns.heatmap(
    D_t,
    annot=True,
    fmt="d",
    cmap="Greens",
    xticklabels=iris.target_names,
    yticklabels=iris.target_names
)

plt.title("Decision Tree")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.tight_layout()
plt.savefig("Day7/Confusion Matrix.png")
plt.show()