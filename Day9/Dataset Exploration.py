'''Load the Iris dataset.
Convert it into a Pandas DataFrame.
Explore the dataset.'''

import pandas as pd 
from sklearn.datasets import load_iris
data=load_iris()
print(data.keys())
print(data.feature_names)
x=data.data
df=pd.DataFrame(data.data,columns=data.feature_names)
print(df)
print(df.shape)
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())