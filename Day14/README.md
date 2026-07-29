# Day-14: OpenCV Fundamentals & Image Processing Toolkit

## Overview

This project demonstrates the fundamentals of OpenCV by implementing various image processing operations using Python. It also includes a Gradio-based Image Processing Toolkit that provides a user-friendly interface for performing image manipulations such as grayscale conversion, resizing, rotation, flipping, cropping, drawing shapes, adding text, and downloading the processed image.

---

## Objectives

The main objectives of this project are:

- Learn the basics of OpenCV.
- Understand image properties and color spaces.
- Perform common image processing operations.
- Build an interactive Image Processing Toolkit using Gradio.

---

# Topics Covered

## OpenCV Fundamentals

- Introduction to OpenCV
- Reading Images
- Displaying Images
- Saving Images
- Image Properties
- Height
- Width
- Number of Channels
- File Size
- BGR vs RGB
- Grayscale Images

---

## Basic Image Operations

The following image processing operations were implemented:

- Resize Image
- Crop Image
- Rotate Image (90°, 180°, 270°)
- Flip Image (Horizontal & Vertical)
- Draw Rectangle
- Draw Circle
- Draw Line
- Draw Polygon
- Add Custom Text
- Save Processed Image

---

## Coding Practice

The following OpenCV programs were created:

- Read an image and display its dimensions.
- Display image height, width, number of channels, and file size.
- Convert a color image to grayscale.
- Resize an image to multiple resolutions.
- Crop different regions of an image.
- Rotate an image by 90°, 180°, and 270°.
- Flip an image horizontally and vertically.
- Draw geometric shapes:
  - Rectangle
  - Circle
  - Line
  - Polygon
- Add custom text (Name and Date).
- Save all processed images inside the **Output** folder.

---

# Mini Project

## Image Processing Toolkit

An interactive Image Processing Toolkit was developed using **Python, OpenCV, and Gradio**.

### Features

- Upload an Image
- Convert to Grayscale
- Resize Image
- Rotate Image
- Flip Image
- Crop Image
- Draw Shapes
- Add Custom Text
- Select Shape Color (BGR)
- Adjust Thickness
- Download Processed Image
- Clear All Inputs
- Save Processed Image

---

# Technologies Used

- Python 3
- OpenCV
- NumPy
- Gradio

---

# Folder Structure

```
Day-14/
│
├── OpenCV Practice Programs/
│
├── Image Processing Toolkit(Command line Interface)/
│
├── Sample Input Images/
│
├──Output_Images/
│
├── README.md
│
├──app.py (Graio app)
│
└── requirements.txt
```

---

# Difference Between BGR and RGB

BGR and RGB are two different color formats used to represent color images.

### RGB

- Stands for Red, Green, Blue.
- Used by most image processing libraries and display systems.
- Matplotlib and PIL display images in RGB format.

Example:

```
(Red, Green, Blue)
(255, 0, 0)
```

---

### BGR

- Stands for Blue, Green, Red.
- OpenCV stores images in BGR format by default.

Example:

```
(Blue, Green, Red)
(255, 0, 0)
```

This value represents **Blue** in OpenCV, whereas the same value represents **Red** in RGB.

### Conversion

```python
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
```

---

# What is a Grayscale Image?

A grayscale image contains only intensity information instead of color information.

Each pixel has only one value ranging from:

```
0 → Black
255 → White
```

Grayscale images require less memory and are commonly used for:

- Edge Detection
- Object Detection
- Face Detection
- Image Thresholding
- Computer Vision Tasks

### Conversion

```python
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
```

---

# OpenCV Functions Used

The following OpenCV functions were used in this project:

| Function | Purpose |
|----------|---------|
| `cv2.imread()` | Read Image |
| `cv2.imshow()` | Display Image |
| `cv2.imwrite()` | Save Image |
| `cv2.cvtColor()` | Convert Color Spaces |
| `cv2.resize()` | Resize Image |
| `cv2.rotate()` | Rotate Image |
| `cv2.flip()` | Flip Image |
| `cv2.rectangle()` | Draw Rectangle |
| `cv2.circle()` | Draw Circle |
| `cv2.line()` | Draw Line |
| `cv2.polylines()` | Draw Polygon |
| `cv2.putText()` | Add Text |

---

# Challenges Faced

During this project, several challenges were encountered:

- Understanding the difference between BGR and RGB color formats.
- Managing dynamic UI visibility in Gradio.
- Handling different image operations within a single application.
- Implementing image download functionality.
- Clearing all Gradio components correctly.
- Managing drawing parameters such as color, thickness, and coordinates.

---

# Solutions

The following solutions were implemented:

- Used `cv2.cvtColor()` for BGR ↔ RGB conversion.
- Used `operation.change()` in Gradio to show only the required controls.
- Implemented a single processing function to handle multiple operations.
- Added download functionality using Gradio File component.
- Used `ClearButton` to reset the interface.
- Added customizable color and thickness options for drawing tools.

---

# Learning Outcomes

After completing this project, I learned:

- OpenCV fundamentals
- Image manipulation techniques
- Color space conversions
- Image drawing functions
- Gradio interface development
- Building an interactive image processing application
- Saving and downloading processed images

---

# Conclusion

This project provided practical experience with OpenCV image processing techniques and Gradio application development. It strengthened my understanding of image manipulation, computer vision basics, and building interactive Python applications.

---

# 👨‍💻 Author

**Muhammad Asad Ali**