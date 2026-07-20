'''Breast Cancer Prediction System

For this project, use the Breast Cancer Wisconsin Diagnostic Dataset, which is built into the Scikit-learn library. There is no need to download the dataset separately.
Build a complete classification pipeline that:

Loads the dataset.
Preprocesses the data.
Trains a Logistic Regression model.
Performs Hyperparameter Tuning using GridSearchCV.
Evaluates the model before and after tuning.
Prints the best parameters selected by GridSearchCV.
Displays the final evaluation metrics.

Bonus (Optional):

Create a confusion matrix heatmap and compare the baseline and tuned model results.'''


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import precision_score,accuracy_score,recall_score,f1_score,classification_report,confusion_matrix

data = load_breast_cancer()
x=data.data
y=data.target
unique, counts = np.unique(y, return_counts=True)  # Check distribtution of target classes
print(dict(zip(unique, counts)))
df=pd.DataFrame(data.data,columns=data.feature_names)
df["target"]=data.target     
print(df.head())      # dataset exploration
print(df.info())
print(df.describe())
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
# baseline model because it trained default parameters whereas received from algorithm (logistic regression)
model=LogisticRegression()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
b_pre=precision_score(y_test,y_pred)
param_grid = {
    "C":[0.01,0.1,1,10,100],  # for regularization 
    "solver":["liblinear","lbfgs"]  # for optimization
}
grid = GridSearchCV(
    estimator=model,
    param_grid=param_grid,
    cv=5
)
grid.fit(X_train,y_train)
print(grid.best_params_)
best_model=grid.best_estimator_  # stored best parameter model with high evalaution scored in best_model again not need to manually add again parameter so direct use this tuned model
y_best_model=best_model.predict(X_test)  

print("Best parameter selected by GridSearchCV ") # selected hyperparameter by gridsearchcv
print(grid.best_params_)
print("Evaluation & Confusion metrics of baseline models") # for baseline model
print(" precision of baseline model is : ",b_pre)
b_acc=accuracy_score(y_test,y_pred)
print(" accuracy of baseline model is : ",b_acc)
b_re=recall_score(y_test,y_pred)
print(" Recall of baseline model is : ",b_re)
b_f1=f1_score(y_test,y_pred)
print(" F1 of baseline model is : ",b_f1)

print("Evaluation & Confusion metrics of Tuned models") # for tuned model
b_pre_b=precision_score(y_test,y_best_model)
print(" precision of baseline model is : ",b_pre_b)
b_acc_b=accuracy_score(y_test,y_best_model)
print(" accuracy of baseline model is : ",b_acc_b)
b_re_b=recall_score(y_test,y_best_model)
print(" Recall of baseline model is : ",b_re_b)
b_f1_b=f1_score(y_test,y_best_model)
print(" F1 of baseline model is : ",b_f1_b)

c_baseline=confusion_matrix(y_test,y_pred)
c_tuned=confusion_matrix(y_test,y_best_model)
print(c_baseline)
print(c_tuned)
label=data.target_names
plt.subplot(1,2,1)
sns.heatmap(
    c_baseline,
    annot=True,
    fmt="d",
    cmap="YlOrBr",
    xticklabels=label,
    yticklabels=label
)

plt.title("Baseline Mode")
plt.xlabel("Predicted")
plt.ylabel("Actual")

# Decision Tree heatmap,
plt.subplot(1,2,2)

sns.heatmap(
    c_tuned,
    annot=True,
    fmt="d",
    cmap="Oranges",
    xticklabels=label,
    yticklabels=label
)

plt.title("Hyper_parameter (Tuned Model)")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.tight_layout()
plt.savefig("Day8/basline & tuned model matrix.png")
plt.show()

