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
import tensorflow_datasets as tfds

#Practice 1

base_model = MobileNetV2(
    weights="imagenet",                # Load ImageNet trained weights
    include_top=False,                 # Remove original classifier
    input_shape=(224, 224, 3)          # Input image size
)

base_model.summary()

base_model.trainable=False
model = keras.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(128, activation="relu"),
    layers.Dropout(0.3),
    layers.Dense(2, activation="softmax")
])  

#Practice 2

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