# 📄 Document Image Enhancement Tool

## Overview

The **Document Image Enhancement Tool** is a Gradio-based Python application that improves the quality of document images captured using a mobile phone or camera. The application automatically detects the document, corrects its perspective if it is tilted, reduces noise, enhances brightness and contrast, sharpens the image, and displays the enhanced result.

---

# Features

* Upload a document image.
* Automatically detect and correct document perspective.
* Convert the document to grayscale.
* Reduce image noise.
* Enhance brightness and contrast using CLAHE.
* Sharpen the image for better readability.
* Display the enhanced document.

---

# Transformations Implemented

## 1. Perspective Transformation (Deskew)

**Purpose:**

Perspective Transformation corrects the shape of a tilted document captured from an angle. It converts the document into a straight, top-down view.

**OpenCV Functions Used:**

* `cv2.findContours()`
* `cv2.approxPolyDP()`
* `cv2.getPerspectiveTransform()`
* `cv2.warpPerspective()`

**Result:**

The document becomes properly aligned and easier to read.

---

## 2. Grayscale Conversion

**Purpose:**

The image is converted from color to grayscale because document processing mainly requires text information rather than color information.

**OpenCV Function Used:**

* `cv2.cvtColor()`

**Result:**

Removes unnecessary color information and simplifies further processing.

---

# Enhancement Techniques

## 1. Noise Reduction

**Technique Used:**

`cv2.fastNlMeansDenoisingColored()`

**Purpose:**

Removes random image noise while preserving important edges and text.

**Benefit:**

Produces a cleaner document without significantly affecting text quality.

---

## 2. Brightness Enhancement

**Technique Used:**

`cv2.convertScaleAbs()`

**Purpose:**

Increases image brightness to improve visibility in dark document images.

---

## 3. Contrast Enhancement

**Technique Used:**

CLAHE (Contrast Limited Adaptive Histogram Equalization)

**OpenCV Function Used:**

`cv2.createCLAHE()`

**Purpose:**

Improves local contrast without over-amplifying noise.

**Benefit:**

Makes faded text more readable.

---

## 4. Image Sharpening

**Technique Used:**

Unsharp Masking

**OpenCV Functions Used:**

* `cv2.GaussianBlur()`
* `cv2.addWeighted()`

**Purpose:**

Enhances document edges and text by emphasizing fine details.

**Benefit:**

Produces sharper and clearer text.

---

# Which Transformation Had the Biggest Impact?

The **Perspective Transformation** had the biggest impact on document quality.

Before perspective correction, the document appeared tilted and distorted due to the camera angle. After applying perspective transformation, the document became straight and properly aligned, making the remaining enhancement steps more effective and improving overall readability.

---

# Challenges Faced During Implementation

During the implementation of this project, several challenges were encountered:

* Detecting the correct document contour when multiple objects were present in the image.
* Automatically identifying the four document corners accurately.
* Choosing appropriate Canny Edge Detection thresholds.
* Balancing brightness and contrast without over-enhancing the image.
* Applying sharpening without introducing excessive noise.
* Preserving document quality while reducing image noise.

These challenges were addressed using contour detection, polygon approximation, CLAHE, Non-Local Means Denoising, and Unsharp Masking techniques.

---

# Technologies Used

* Python
* OpenCV
* NumPy
* Gradio

---

# Output Pipeline

```text
Input Document
      │
      ▼
Perspective Correction
      │
      ▼
Grayscale Conversion
      │
      ▼
Noise Reduction
      │
      ▼
Brightness Enhancement
      │
      ▼
Contrast Enhancement (CLAHE)
      │
      ▼
Image Sharpening
      │
      ▼
Enhanced Document
```

---

# Conclusion

This project demonstrates a complete document enhancement pipeline using OpenCV and Gradio. By combining perspective correction, grayscale conversion, noise reduction, brightness adjustment, CLAHE-based contrast enhancement, and image sharpening, the application produces clean, readable, and high-quality document images suitable for scanning, archiving, and OCR applications.

---

# 👨‍💻 Author

**Muhammad Asad Ali**