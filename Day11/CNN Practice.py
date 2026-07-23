'''
Coding Practice

Using TensorFlow/Keras:

Practice 1

Load the Fashion MNIST dataset.
Visualize at least 10 sample images with their labels.
Normalize the dataset.

Practice 2

Build a simple CNN model that includes:

Convolution Layer
Max Pooling Layer
Flatten Layer
Dense Layers
Output Layer

Train the model and observe the training progress.

Practice 3

Evaluate the trained model using:

Training Accuracy
Test Accuracy
Loss
Predictions on sample images'''

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras import layers
import matplotlib.pyplot as plt
import numpy as np

# practice 1
(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()   # first data load then split training and testing

class_names = [      #$Visualize at least 10 sample images with their labels.
    "T-shirt/Top",
    "Trouser",
    "Pullover",
    "Dress",
    "Coat",
    "Sandal",
    "Shirt",
    "Sneaker",
    "Bag",
    "Ankle Boot"
]
plt.figure(figsize=(10,5))
for i in range(10):
    plt.subplot(2,5,i+1)
    plt.imshow(X_train[i], cmap="gray")
    plt.title(class_names[y_train[i]])
    plt.axis("off")
plt.tight_layout()
plt.show()

X_train = X_train / 255.0     # for normalization 
X_test = X_test / 255.

X_train = X_train.reshape(-1, 28, 28, 1)
X_test = X_test.reshape(-1, 28, 28, 1)

model=keras.Sequential([
    layers.Input(shape=(28,28,1)),

    layers.Conv2D(32, (3,3), activation='relu'),
    layers.MaxPooling2D((2,2)),
    layers.Conv2D(64, (3,3), activation='relu'),
    layers.MaxPooling2D((2,2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Model Summary
model.summary()

# Compile Model
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
train_model=model.fit(
    X_train,
    y_train,
    epochs=10,
    batch_size=32,
    validation_split=0.2
)   
pred_model=model.predict(X_test)

# showa 10 predicted images with actual images  (sample prediction )
plt.figure(figsize=(12,6))
for i in range(10):
    plt.subplot(2,5,i+1)
    plt.imshow(X_test[i], cmap="gray")
    predicted_label = np.argmax(pred_model[i])
    actual_label = y_test[i]
    plt.title(
        f"P: {class_names[predicted_label]}\nA: {class_names[actual_label]}",
        fontsize=9
    )
    plt.axis("off")
plt.tight_layout()     
plt.show()


#Shows model evaluation
# Training Accuracy
train_loss, train_accuracy = model.evaluate(X_train, y_train)
print("Training Accuracy :", train_accuracy)
print("Training Loss :", train_loss)

# Test Accuracy
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print("\nTest Accuracy :", test_accuracy)
print("Test Loss :", test_loss)