
# Breast Cancer Wisconsin Diagnostic Dataset in Scikit-Learn
# import dataset 
# Dataset Eploration
# Check distribution of Target Classes

import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer
data = load_breast_cancer()
x=data.data
y=data.target
print(data.feature_names)
print(data.target_names)
unique, counts = np.unique(y, return_counts=True)  # Check distribtution of target classes
print(dict(zip(unique, counts)))
df=pd.DataFrame(data.data,columns=data.feature_names)
df["target"]=data.target     
print(df.head())      # dataset exploration
print(df.info())
print(df.describe())
print(df.shape)

