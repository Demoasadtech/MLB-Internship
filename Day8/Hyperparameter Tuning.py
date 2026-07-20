#Hyperparamter & tuned model

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import precision_score,accuracy_score,recall_score,f1_score,classification_report
data = load_breast_cancer()
x=data.data
y=data.target
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
model=LogisticRegression()
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

print("Evaluation & Confusion metrics of Tuned models") # for tuned model
b_pre_b=precision_score(y_test,y_best_model)
print(" precision of baseline model is : ",b_pre_b)
b_acc_b=accuracy_score(y_test,y_best_model)
print(" accuracy of baseline model is : ",b_acc_b)
b_re_b=recall_score(y_test,y_best_model)
print(" Recall of baseline model is : ",b_re_b)
b_f1_b=f1_score(y_test,y_best_model)
print(" F1 of baseline model is : ",b_f1_b)
