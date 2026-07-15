# 📘 Day 6 - Data Preprocessing & Linear Regression

## 📌 Objective

The objective of this project is to understand the complete Machine Learning workflow, including data preprocessing, feature selection, train-test splitting, feature scaling, and building a Linear Regression model using Scikit-learn.

---

## 📂 Project Files

- Data Preprocessing.py
- Linear Regression Model.py
- Student Score Prediction.py
- dirty_student_records.csv
- After_Data_Preprocessing.csv
- actual_vs_predicted.png
- requirements.txt

---

## 📚 Topics Covered

- Data Preprocessing
- Features and Target Variables
- Handling Missing and Invalid Values
- Feature Scaling (StandardScaler)
- Train-Test Split
- Data Leakage
- Introduction to Scikit-learn
- Linear Regression
- Model Evaluation
- Data Visualization

---

## 🛠 Data Preprocessing

The following preprocessing steps were performed:

- Loaded the student dataset.
- Removed extra spaces from column names.
- Converted subject columns to numeric values.
- Replaced invalid values (marks less than 0 or greater than 100) with missing values.
- Filled missing values using the mean of each subject.
- Renamed incorrect column names.
- Created the **Average_Score** column by calculating the average of the five subject marks.
- Removed unnecessary columns:
  - Rank
  - Roll_No
  - Name
  - Total_marks

---

## 🎯 Feature and Target Selection

### Features (X)

- Machine Learning
- Robotics_design
- Digital_Electronics
- Feedback_Control_System
- Computer_Architecture

### Target (y)

- Average_Score

---

## ✂ Train-Test Split

The dataset was divided into:

- **80% Training Data**
- **20% Testing Data**

```python
test_size = 0.2
random_state = 42
```

Using `random_state=42` ensures the same train-test split every time the code is executed.

---

## ⚖ Feature Scaling

Feature scaling was performed using **StandardScaler**.

```python
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```

Only the feature columns were scaled.

The target column (**Average_Score**) was not scaled because Linear Regression predicts the target in its original scale.

---

## 🤖 Machine Learning Model

Algorithm Used:

- **Linear Regression**

Steps performed:

- Created the model
- Trained the model using training data
- Predicted Average Scores on the test dataset

---

## 📊 Model Evaluation

The following evaluation metrics were used:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- R² Score

### Model Performance

- MAE: Very Low
- MSE: Very Low
- R² Score: Approximately **1.00**

The model achieved excellent performance because the target variable (**Average_Score**) was calculated directly from the five subject marks, resulting in a strong linear relationship.

---

## 📈 Visualization

A scatter plot was created to compare:

- Actual Values
- Predicted Values

Most data points lie very close to the diagonal line, indicating highly accurate predictions.

---

## 📖 What I Learned

During this project, I learned:

- Why data preprocessing is important.
- How to clean a dataset before training a model.
- The difference between features and target variables.
- Why train-test splitting is necessary.
- What data leakage is and how to avoid it.
- How feature scaling works using StandardScaler.
- How Linear Regression learns relationships between variables.
- How to evaluate a Machine Learning model using MAE, MSE, and R² Score.
- How to visualize prediction results using a scatter plot.

---

## 📌 Conclusion

This project demonstrates the complete Machine Learning workflow using Scikit-learn. Proper data preprocessing significantly improved data quality, allowing the Linear Regression model to achieve highly accurate predictions. The project also highlights the importance of train-test splitting, feature scaling, and evaluation metrics in building reliable Machine Learning models.

---

## Author

**Muhammad Asad Ali**