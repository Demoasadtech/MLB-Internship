'''Using TensorFlow/Keras:

Practice 1

Load a pre-trained MobileNetV2 model.
Explore its architecture.
Freeze the base model layers.
Add your own classification head.

Practice 2

Load the Cats vs Dogs dataset using TensorFlow Datasets (TFDS).
Preprocess and resize the images.
Split the dataset into training and validation sets.'''

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.applications import MobileNetV2
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import tensorflow_datasets as tfds

base_model = MobileNetV2(
    weights="imagenet",                # Load ImageNet trained weights
    include_top=False,                 # Remove original classifier
    input_shape=(224, 224, 3)          # Input image size
)

#base_model summary
base_model.summary()


base_model.trainable=False
model = keras.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(128, activation="relu"),
    layers.Dropout(0.3),
    layers.Dense(2, activation="softmax")
])  


dataset, info = tfds.load(
    "cats_vs_dogs",
    with_info=True,
    as_supervised=True
)
total_images = info.splits["train"].num_examples
train_size = int(0.8 * total_images)
train_ds = dataset["train"].take(train_size)
validation_ds = dataset["train"].skip(train_size)

# Image Size
image_size = 224

# Preprocessing Function
def preprocess(image, label):
    image = tf.image.resize(image, (image_size, image_size))
    image = image / 255.0
    return image, label

# Apply Preprocessing
train_ds = train_ds.map(preprocess)
validation_ds = validation_ds.map(preprocess)

# Batch
batch_size = 32

# Apply batch on training and testing data 
train_ds = train_ds.batch(batch_size)    
validation_ds = validation_ds.batch(batch_size)

# Prefetch  basically it automatically fit one batch after another
train_ds = train_ds.prefetch(tf.data.AUTOTUNE)
validation_ds = validation_ds.prefetch(tf.data.AUTOTUNE)
print("Dataset Ready for Training!")


# Compile Model
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]

)


# Train Model
history = model.fit(
    train_ds,
    validation_data=validation_ds,
    epochs=5

)


# Evaluate Model
loss, accuracy = model.evaluate(validation_ds)


# Sample Predictions
class_names = ["Cat", "Dog"]
images, labels = next(iter(validation_ds))
predictions = model.predict(images)
predicted_labels = tf.argmax(predictions, axis=1)
plt.figure(figsize=(12,8))
for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i])
    plt.title(
        f"Actual : {class_names[labels[i]]}\nPred : {class_names[predicted_labels[i]]}"
    )
    plt.axis("off")
plt.tight_layout()
plt.show()


# Plot Accuracy
plt.figure(figsize=(8,5))
plt.plot(history.history["accuracy"], label="Training Accuracy")
plt.plot(history.history["val_accuracy"], label="Validation Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.title("Accuracy Curve")
plt.show()


# Plot Loss
plt.figure(figsize=(8,5))
plt.plot(history.history["loss"], label="Training Loss")
plt.plot(history.history["val_loss"], label="Validation Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.title("Loss Curve")
plt.show()