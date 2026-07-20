
# Baseline model
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import precision_score,accuracy_score,recall_score,f1_score,classification_report
data = load_breast_cancer()
x=data.data
y=data.target
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
# baseline model because it trained default parameters whereas received by algorithm (logistic regression)
model=LogisticRegression()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
print("Evaluation & Confusion matrics of baseline models") # for baseline model
b_pre=precision_score(y_test,y_pred)        # confusion matrics
print(" precision of baseline model is : ",b_pre)
b_acc=accuracy_score(y_test,y_pred)
print(" accuracy of baseline model is : ",b_acc)
b_re=recall_score(y_test,y_pred)
print(" Recall of baseline model is : ",b_re)
b_f1=f1_score(y_test,y_pred)
print(" F1 of baseline model is : ",b_f1)
