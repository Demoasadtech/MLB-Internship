# Day-8: Model Evaluation & Hyperparameter Tuning using Logistic Regression

## 📌 Overview

This project demonstrates the complete Machine Learning workflow for evaluating and improving a classification model using the **Breast Cancer Wisconsin Diagnostic Dataset** available in **Scikit-learn**. The project includes dataset exploration, baseline model creation, hyperparameter tuning using GridSearchCV, model comparison, and confusion matrix visualization.

---

# 📂 Project Structure

```
Day-8/
│
├── Dataset Exploration.py
├── Baseline Model.py
├── Hyperparameter Tuning.py
├── Breast Cancer Prediction.py
├── basline & tuned model matrix.png
├── README.md
└── requirements.txt
```

---

# 📊 Dataset

**Dataset:** Breast Cancer Wisconsin Diagnostic Dataset

**Source:**

```python
from sklearn.datasets import load_breast_cancer
```

### Dataset Information

- Total Samples: **569**
- Features: **30**
- Classes:
  - Malignant (Cancer)
  - Benign (Non-Cancer)

---

# 🚀 Project Workflow

## Step 1: Dataset Exploration

The dataset was loaded from Scikit-learn and converted into a Pandas DataFrame.

The following functions were used:

- `head()`
- `info()`
- `describe()`
- Target class distribution

---

## Step 2: Build a Baseline Model

The dataset was divided into training and testing sets using `train_test_split()`.

A Logistic Regression model with default hyperparameters was trained.

The model was evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

This model serves as the baseline model for comparison.

---

## Step 3: Hyperparameter Tuning

GridSearchCV was used to search for the best hyperparameters.

```python
param_grid = {
    "C": [0.01, 0.1, 1, 10, 100],
    "solver": ["liblinear", "lbfgs"]
}
```

GridSearchCV was configured with:

- 5-Fold Cross Validation
- Accuracy as the scoring metric

After training, the best hyperparameters and the optimized model were selected automatically.

---

# 📈 Model Evaluation

Both the baseline model and tuned model were evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

The evaluation metrics were compared to observe whether hyperparameter tuning improved the model performance.

---

# 🧠 What I Learned About Model Evaluation

Through this project, I learned how to evaluate classification models using different evaluation metrics.

The main concepts learned include:

- Train vs Test Performance
- Underfitting
- Overfitting
- Cross Validation
- Learning Curves
- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

These evaluation techniques help determine how well a model performs on unseen data.

---

# ⚙️ What is Hyperparameter Tuning and Why It Matters

Hyperparameter tuning is the process of selecting the best model settings before training.

Instead of using default values, GridSearchCV tests multiple combinations of hyperparameters and selects the combination that provides the best validation performance.

Hyperparameter tuning helps to:

- Improve model accuracy
- Reduce overfitting
- Reduce underfitting
- Improve generalization
- Automatically select the best-performing model

---

# 🏆 Best Parameters Found by GridSearchCV

Replace the following values with your actual output:

```python
{
    "C": 0.1
    "solver": "liblinear"
}
```

---

## 📊 Baseline vs Tuned Model Comparison

| Metric | Baseline Model | Tuned Model |
|---------|---------------:|------------:|
| Accuracy | **0.973684** | **0.991228** |
| Precision | **0.972222** | **0.986111** |
| Recall | **0.985915** | **1.000000** |
| F1-Score | **0.979021** | **0.993007** |

---

# 🔍 Key Observations

- The baseline Logistic Regression model achieved good performance using default hyperparameters.
- GridSearchCV successfully searched multiple hyperparameter combinations.
- The tuned model selected the optimal values for the Logistic Regression algorithm.
- Hyperparameter tuning improved the model's overall performance and generalization.
- Confusion matrix comparison clearly showed the prediction differences between the baseline and tuned models.

---

# 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

# 📚 Concepts Covered

- Dataset Exploration
- Logistic Regression
- Train-Test Split
- Model Evaluation
- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix
- Cross Validation
- Hyperparameter Tuning
- GridSearchCV
- Baseline vs Tuned Model Comparison

---

# 🎯 Conclusion

This project demonstrates the complete Machine Learning workflow for building, evaluating, and improving a classification model. Hyperparameter tuning using GridSearchCV helped identify the best Logistic Regression configuration, leading to improved model performance compared to the baseline model. The project also reinforced the importance of selecting appropriate evaluation metrics and optimal model parameters for reliable predictions.

---

## Author

**Muhammad Asad Ali**