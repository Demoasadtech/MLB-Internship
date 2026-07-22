# Creat Simple ANN  & perceptron model 
import tensorflow as tf
from tensorflow import keras
model = keras.Sequential([
    keras.layers.Input(shape=(4,)),
    keras.layers.Dense(8, activation="relu"),
    keras.layers.Dense(1, activation="sigmoid")
])
model1 = keras.Sequential([
    keras.layers.Input(shape=(4,)),
    keras.layers.Dense(8, activation="relu"),
    keras.layers.Dense(1, activation="tanh")
])
model2 = keras.Sequential([
    keras.layers.Input(shape=(4,)),
    keras.layers.Dense(8, activation="sigmoid"),
    keras.layers.Dense(1, activation="tanh")
])

model.summary()
model1.summary()
model2.summary()

'''
At the moment, I have only created the input, hidden,
and output layers and experimented with different activation
functions. Since no dataset has been imported and the model 
hasn't been trained yet, the output remains the same. Once'
' the dataset is provided and training begins, each activation'
' function will work differently internally and influence the model's
learning and predictions.'''