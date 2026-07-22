'''Build Your First Artificial Neural Network

For this project, use the Fashion MNIST Dataset, which is built into TensorFlow/Keras.

Load the dataset using:

from tensorflow.keras.datasets import fashion_mnist


Your application should:

Load the Fashion MNIST dataset.
Explore the dataset (shape, labels, sample images).
Normalize the pixel values.
Build a simple Artificial Neural Network (ANN).
Train the model.
Evaluate the model on the test dataset.
Display the training and validation accuracy.
Make predictions on a few test images.
Display the predicted and actual labels.

Bonus (Optional):

Plot the training and validation accuracy curves.
Display a few sample predictions with their corresponding images.'''

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.datasets import fashion_mnist
import matplotlib.pyplot as plt
import numpy as np

(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()   # first data load then split training and testing

print("Training Images Shape:", X_train.shape)    # find matrix dimensions
print("Training Labels Shape:", y_train.shape)
print("Testing Images Shape:", X_test.shape)
print("Testing Labels Shape:", y_test.shape)
print("\nFirst 10 Labels:")
#print(y_train[:10])

class_names = [
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

model = keras.Sequential([     # create layer 
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(128, activation="relu"),
    keras.layers.Dense(64, activation="relu"),
    keras.layers.Dense(10, activation="softmax")
])

print("\nModel Summary")
model.summary()    # print summary 
model.compile(    # compile model
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

history = model.fit(    # fit data for training
    X_train,
    y_train,
    epochs=10,
    validation_split=0.2
)
predictions = model.predict(X_test)

plt.figure(figsize=(12,6))
for i in range(10):
    plt.subplot(2,5,i+1)
    plt.imshow(X_test[i], cmap="gray")
    predicted_label = np.argmax(predictions[i])
    actual_label = y_test[i]
    plt.title(
        f"P: {class_names[predicted_label]}\nA: {class_names[actual_label]}",
        fontsize=9
    )
    plt.axis("off")

plt.tight_layout()       # showa 10 predicted images with actual images
plt.savefig("Day10/Generated Graph & images/predicted first 10 ")
plt.show()

index = 15    # predict and test only one image
predicted_label = np.argmax(predictions[index])
print("\nPrediction for Image:", index)
print("Predicted Label :", class_names[predicted_label])
print("Actual Label    :", class_names[y_test[index]])
plt.figure(figsize=(4,4))
plt.imshow(X_test[index], cmap="gray")
plt.title(
    f"Predicted: {class_names[predicted_label]}\nActual: {class_names[y_test[index]]}"
)
plt.axis("off")
plt.savefig("Day10/Generated Graph & images/predicted one image")
plt.show()


plt.figure(figsize=(8,5))

plt.plot(history.history["accuracy"], label="Training Accuracy", marker="o")
plt.plot(history.history["val_accuracy"], label="Validation Accuracy", marker="o")

plt.title("Training vs Validation Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")

plt.legend()
plt.grid(True)
plt.savefig("Day10/Generated Graph & images/training accuracy graph")
plt.show()