# Day-12: Transfer Learning - Cats vs Dogs Image Classifier

## 📌 Project Overview

This project demonstrates the use of **Transfer Learning** for image classification using **MobileNetV2** as a pre-trained CNN model. The model is trained on the **Cats vs Dogs** dataset provided by TensorFlow Datasets (TFDS).

---

# 📚 What is Transfer Learning?

Transfer Learning is a deep learning technique in which a model that has already been trained on a large dataset (such as ImageNet) is reused for a new but related task.

Instead of training a CNN from scratch, we use the knowledge learned by the pre-trained model and add our own classifier for the new dataset.

---

# ❓ Why Transfer Learning?

Transfer Learning is used because:

- It requires less training time.
- It performs well even with smaller datasets.
- It reduces computational cost.
- It provides higher accuracy than training from scratch.
- It takes advantage of features already learned from millions of images.

---

# 🚀 Why MobileNetV2?

I selected **MobileNetV2** because:

- It is lightweight and fast.
- It provides high accuracy with low computational cost.
- It is optimized for mobile and edge devices.
- It performs well for transfer learning tasks.
- It requires less memory compared to larger CNN models.

---

# 🛠️ Project Workflow

1. Loaded the Cats vs Dogs dataset using TensorFlow Datasets.
2. Split the dataset into training and validation sets.
3. Resized all images to **224 × 224**.
4. Normalized image pixel values.
5. Loaded the pre-trained MobileNetV2 model.
6. Removed the original classification head.
7. Froze the base model layers.
8. Added custom classification layers.
9. Trained the model.
10. Evaluated the model.
11. Displayed sample predictions.
12. Plotted training and validation accuracy and loss graphs.

---

# 🧪 Experiments Performed

To improve model performance, the following experiments were performed:

- Increased the number of training epochs.
- Tested different batch sizes.
- Used the Adam optimizer.
- Applied image normalization.
- Used Dropout to reduce overfitting.
- Froze the MobileNetV2 base model.


---

# 📊 Final Results

- **Training Accuracy:** 99.1%
- **Validation Accuracy:** 98.5%
- **Training Loss:** 0.023
- **Validation Loss:** 0.043

The model successfully achieved the required validation accuracy and exceeded the project target.

---

# ⚠️ Challenges Faced

- Understanding Transfer Learning concepts.
- Working with TensorFlow Datasets (TFDS).
- Understanding Feature Extractio
- Handling dataset preprocessing.  

---

# 📖 Lessons Learned

During this project I learned:

- Transfer Learning concepts.
- Feature Extraction.
- Fine-Tuning.
- MobileNetV2 architecture.
- TensorFlow Datasets (TFDS).
- Image preprocessing.
- Model evaluation.
- Accuracy and Loss curve analysis.
- Transfer Learning workflow using TensorFlow/Keras.

---

# 📂 Project Files

```
Day-12/
│
├── Transfer Learning Practice.py
├── Cats_vs_Dogs_Classifier.py
├── README.md
├── Sample & Graphs (Folder)
└── requirements.txt
```

---

# 🛠 Technologies Used

- Python
- TensorFlow
- TensorFlow Datasets (TFDS)
- Keras
- MobileNetV2
- NumPy
- Matplotlib

---

# 🎯 Conclusion

Transfer Learning significantly reduces training time while providing excellent performance. Using MobileNetV2 as a pre-trained backbone allowed the model to achieve high validation accuracy with minimal training, making it an efficient solution for image classification tasks.

---

# 👨‍💻 Author

**Muhammad Asad Ali**