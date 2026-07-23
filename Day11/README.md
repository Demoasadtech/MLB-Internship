# Day 11 - Convolutional Neural Networks (CNN) | Fashion MNIST Image Classification

## 📌 Objective

The objective of this project is to understand the fundamentals of Convolutional Neural Networks (CNNs) and build an image classification model using the Fashion MNIST dataset in TensorFlow/Keras.

---

## 📖 Topics Covered

- Convolutional Neural Networks (CNN)
- Why CNNs are better than ANNs for image data
- Convolution Layer
- Filters (Kernels)
- Feature Maps
- Max Pooling Layer
- Average Pooling Layer
- Flatten Layer
- Fully Connected (Dense) Layer
- Image Classification Workflow
- Training vs Validation Data
- Epochs and Batch Size
- Overfitting in Deep Learning
- Data Augmentation (Concept)
- Model Evaluation

---

# Why CNNs are Better than ANNs

Artificial Neural Networks (ANNs) are not suitable for image data because they flatten images into a one-dimensional vector, which removes the spatial relationship between neighboring pixels. This results in a very large number of parameters and higher chances of overfitting.

Convolutional Neural Networks (CNNs) preserve the spatial structure of images by using convolution filters. CNNs automatically learn important features such as edges, textures, shapes, and objects while using far fewer parameters than ANNs.

---

# Purpose of Convolution Layer

The Convolution Layer applies filters (kernels) over the input image to detect useful features like:

- Edges
- Corners
- Textures
- Patterns
- Shapes

These extracted features are stored as feature maps and passed to the next layers.

---

# Purpose of Pooling Layer

Pooling reduces the spatial size of feature maps while preserving important information.

Benefits:

- Reduces computation
- Reduces memory usage
- Helps prevent overfitting
- Makes the model more robust

Max Pooling selects the maximum value from each region, while Average Pooling calculates the average value.

---

# Model Architecture

```python
Input Layer (28×28×1)

↓

Conv2D (32 Filters, 3×3, ReLU)

↓

MaxPooling2D (2×2)

↓

Conv2D (64 Filters, 3×3, ReLU)

↓

MaxPooling2D (2×2)

↓

Flatten

↓

Dense (128, ReLU)

↓

Dense (10, Softmax)
```

---

# Dataset

- Dataset: Fashion MNIST
- Training Images: 60,000
- Testing Images: 10,000
- Image Size: 28 × 28
- Classes: 10

Classes include:

- T-shirt/Top
- Trouser
- Pullover
- Dress
- Coat
- Sandal
- Shirt
- Sneaker
- Bag
- Ankle Boot

---

# Project Workflow

1. Load Fashion MNIST dataset.
2. Display sample images with labels.
3. Normalize pixel values.
4. Build the CNN model.
5. Train the model.
6. Evaluate model performance.
7. Predict sample images.
8. Plot training and validation accuracy.
9. Display confusion matrix.
10. Show correctly and incorrectly classified images.

---

# Results

## Training Accuracy


```
Training Accuracy: 95.5%
```

## Test Accuracy

> Add your final testing accuracy here.

Example:

```
Test Accuracy: 91.8%
```

## Loss


Example:

```
Loss: 0.32
```

---

# Model Evaluation

The trained CNN model was evaluated using:

- Training Accuracy
- Validation Accuracy
- Test Accuracy
- Loss
- Confusion Matrix
- Predictions on Sample Images

---

# Challenges Faced

- Understanding how convolution filters work.
- Understanding feature maps and pooling.
- Choosing suitable hyperparameters.
- Understanding overfitting and data augmentation.

---

# How the Challenges Were Solved

- Practiced CNN architecture step by step.
- Learned how filters extract image features.
- Used MaxPooling to reduce computation.
- Understood how data augmentation improves generalization.

---

# Deliverables

- ✅ CNN Practice Script
- ✅ Fashion MNIST Classifier Script
- ✅ Generated images & Graphs (Folder)
- ✅ README.md
- ✅ requirements.txt

---

# Technologies Used

- Python
- TensorFlow
- Keras
- NumPy
- Matplotlib
- Scikit-learn

---

# Conclusion

This project provided hands-on experience with Convolutional Neural Networks for image classification. I learned how convolution, pooling, flatten, and dense layers work together to classify images. I also understood why CNNs outperform ANNs for image data and gained practical experience in evaluating deep learning models using accuracy, loss, prediction results, and confusion matrices.


---

# 👨‍💻 Author

**Muhammad Asad Ali**