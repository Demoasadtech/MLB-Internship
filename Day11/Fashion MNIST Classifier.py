'''Fashion MNIST Image Classifier using CNN

Use the Fashion MNIST dataset available in TensorFlow/Keras.

Load the dataset using:

from tensorflow.keras.datasets import fashion_mnist


Build a CNN model that:

Loads and preprocesses the dataset.
Displays sample images.
Trains a CNN for image classification.
Evaluates the model on the test dataset.
Predicts the class of sample images.
Displays both the predicted and actual labels.
Plots the training and validation accuracy curves.
Display a confusion matrix.
Show 10 correctly classified and 10 incorrectly classified images with their predicted labels.'''


# Import All Libraries
import tensorflow as tf            
from tensorflow import keras
from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras import layers
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# first data load then split training and testing
(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()   

#Visualize at least 10 sample images with their labels.
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
# Visualize total 10 labels with names
plt.figure(figsize=(10,5))   
for i in range(10):
    plt.subplot(2,5,i+1)
    plt.imshow(X_train[i], cmap="gray")
    plt.title(class_names[y_train[i]])
    plt.axis("off")
plt.tight_layout()
plt.savefig("Day11/Generated images & Graphs/10 labels with names.png") 
plt.show()

# for normalization
X_train = X_train / 255.0 
X_test = X_test / 255.0

# reshape of 28 X 28 matrix pixel because CNN expect for parameters values (images , height , width , channel= color it means 1 color in Mnist becuase images is gray scale so is 1 whereas 3 in RGB
X_train = X_train.reshape(-1, 28, 28, 1)
X_test = X_test.reshape(-1, 28, 28, 1)
print(X_train.shape)   # check shape
print(X_test.shape)   # check shape


# created layersa input ,hidden ,output layer
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


model.summary()    # Model Summary


model.compile(     # Compile Model
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

train_model=model.fit(    # model train on training data
    X_train,
    y_train,
    epochs=10,
    batch_size=32,
    validation_split=0.2
)

#Calculate loss and accuracy on testing data
loss, accuracy= model.evaluate(X_test,y_test)   
print("total accuracy is : ", accuracy)
print("\ntotal loss is : ", loss)   

#model prediction on testing data
pred_model=model.predict(X_test)  

#Checking 10 images predicted and Actual
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
plt.savefig("Day11/Generated images & Graphs/images predicted and Actual.png")    
plt.show() 

#Visualize of  training and validation accuracy curves.
plt.figure(figsize=(8,5))
plt.plot(train_model.history["accuracy"], label="Training Accuracy", marker="o")
plt.plot(train_model.history["val_accuracy"], label="Validation Accuracy", marker="o")
plt.title("Training vs Validation Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.grid(True)
plt.savefig("Day11/Generated images & Graphs/training and validation accuracy curves.png")    
plt.show()

#Visualize of  training loss and validation loss accuracy curves.
plt.figure(figsize=(8,5))
plt.plot(train_model.history["loss"], label="Training Loss", marker="o")
plt.plot(train_model.history["val_loss"], label="Validation Loss", marker="o")
plt.title("Training vs Validation Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.grid(True)
plt.savefig("Day11/Generated images & Graphs/training loss and validation loss accuracy curves.png") 
plt.show()

#Created Confusion matrix
pred=np.argmax(pred_model, axis=1)   
con_matrix=confusion_matrix(y_test,pred)
print(con_matrix)

#Visualize Confusion matrix
plt.figure(figsize=(10,8))
sns.heatmap(
    con_matrix,
    annot=True,
    fmt='d',
    cmap='Blues',
    xticklabels=class_names,
    yticklabels=class_names
)
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.title("Confusion Matrix")
plt.savefig("Day11/Generated images & Graphs/Confusion matrix.png") 
plt.show()

#Check 10 correct prediction
correct = np.where(pred == y_test)[0]
plt.figure(figsize=(15,8))
for i in range(10):
    index = correct[i]
    plt.subplot(2,5,i+1)
    plt.imshow(X_test[index], cmap="gray")
    plt.title(
        f"Correct\n{class_names[pred[index]]}"
    )
    plt.axis("off")
plt.suptitle("10 Correctly Classified Images")
plt.tight_layout()
plt.savefig("Day11/Generated images & Graphs/10 correct prediction.png")
plt.show()

#Check 10 Wrong prediction
incorrect = np.where(pred != y_test)[0]
plt.figure(figsize=(15,8))
for i in range(10):
    index = incorrect[i]
    plt.subplot(2,5,i+1)
    plt.imshow(X_test[index], cmap="gray")
    actual = class_names[y_test[index]]
    predicted = class_names[pred[index]]
    plt.title(
        f"A:{actual}\nP:{predicted}",
        fontsize=9
    )
    plt.axis("off")
plt.suptitle("10 Incorrectly Classified Images")
plt.tight_layout()
plt.savefig("Day11/Generated images & Graphs/10 Wrong prediction.png")
plt.show()