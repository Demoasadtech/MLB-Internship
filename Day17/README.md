# Shape Detection System using OpenCV and Gradio

## 📌 Project Overview

This project is a Python-based Shape Detection System developed using **OpenCV** and **Gradio**.

The application allows users to upload an image containing geometric shapes. It detects each shape, draws contours, labels the detected shape, calculates its area and perimeter, and displays the final processed image.

---

# Features

- Upload an image using Gradio
- Detect contours
- Detect multiple shapes
- Draw contours around each shape
- Display shape labels
- Calculate contour area
- Calculate contour perimeter
- Show bounding rectangle
- Display the final output image

---

# Shapes Detected

The application can detect the following shapes:

- Triangle
- Square
- Rectangle
- Circle
- Polygon

---

# What are Contours?

Contours are the boundaries or outlines of objects in an image.

They are formed by joining all the continuous points having the same intensity. Contours are useful for detecting object shapes, measuring object size, and performing image analysis.

Example:

```
     *********
   **         **
  *             *
  *             *
   **         **
     *********
```

The outer boundary of the object is called a **Contour**.

---

# How Contour Detection Works

The program follows these steps:

1. Load the input image.
2. Convert the image to grayscale.
3. Apply binary thresholding.
4. Detect contours using `cv2.findContours()`.
5. Approximate contour corners using `cv2.approxPolyDP()`.
6. Count the number of corners.
7. Identify the shape.
8. Draw contours.
9. Display shape labels.
10. Calculate area and perimeter.
11. Display the final processed image.

---

# Technologies Used

- Python
- OpenCV
- NumPy
- Gradio

---

# Shape Detection Logic

| Number of Corners | Detected Shape |
|------------------:|----------------|
| 3 | Triangle |
| 4 (Aspect Ratio ≈ 1) | Square |
| 4 (Aspect Ratio ≠ 1) | Rectangle |
| 8 or more | Circle |
| 5–7 | Polygon |

---

# Area and Perimeter

The application calculates:

- Contour Area using `cv2.contourArea()`
- Contour Perimeter using `cv2.arcLength()`

These values are displayed for every detected shape.

---



# Challenges Faced

During the development of this project, I encountered several challenges:

- Detecting circles correctly because they were sometimes identified as polygons.
- Choosing the correct threshold value for different images.
- Differentiating between squares and rectangles using aspect ratio.
- Removing small noisy contours using contour area filtering.
- Handling different image sizes and varying lighting conditions.

These issues were solved by:

- Using `cv2.approxPolyDP()` for contour approximation.
- Filtering small contours using contour area.
- Using the aspect ratio to distinguish squares from rectangles.
- Adjusting threshold values for better contour detection.


---

# Author

**Muhammad Asad Ali**

