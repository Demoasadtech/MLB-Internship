'''Build a Linear Regression model to predict the student's Average_Score.

After training the model:

Make predictions on the test dataset.
Compare Actual vs Predicted values.
Calculate:

  
Mean Absolute Error (MAE)
Mean Squared Error (MSE)
R² Score'''

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import pandas as pd 
df=pd.read_csv("Day6/After_Data_Preprocessing.csv")
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