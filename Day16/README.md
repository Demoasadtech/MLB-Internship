# 📄 Document Boundary Detection Tool

## 📌 Project Overview

This project is a **Document Boundary Detection Tool** built using **Python, OpenCV, and Gradio**.

The application allows users to upload a document image (such as receipts, invoices, scanned pages, ID cards, or printed papers). It processes the image using OpenCV techniques and detects the document boundary by drawing a contour around it.

---

# 🚀 Features

- Upload document images
- Convert image to grayscale
- Apply Gaussian Blur
- Detect edges using Canny Edge Detection
- Apply Morphological Closing to remove noise
- Detect contours
- Find the largest contour
- Draw the detected document boundary
- User-friendly Gradio interface
- Sample images for testing
- Error handling using try-except

---

# 🛠 Technologies Used

- Python
- OpenCV
- NumPy
- Gradio

---

# 📖 Image Processing Pipeline

1. Upload Image
2. Convert RGB to BGR
3. Convert to Grayscale
4. Apply Gaussian Blur
5. Perform Canny Edge Detection
6. Apply Morphological Closing
7. Detect Contours
8. Find the Largest Contour
9. Approximate the Document Boundary
10. Draw the Boundary
11. Display the Final Output

---

# 📚 Difference Between Sobel, Laplacian, and Canny

## Sobel Operator

- Detects horizontal and vertical edges.
- Uses first-order derivatives.
- Good for detecting edge direction.
- More sensitive to noise than Canny.

### Advantages

- Simple
- Fast
- Detects edge direction

### Disadvantages

- Produces noisy edges
- Less accurate

---

## Laplacian Operator

- Detects edges in all directions.
- Uses second-order derivatives.
- Highlights rapid intensity changes.

### Advantages

- Detects edges from every direction.
- Easy to implement.

### Disadvantages

- Very sensitive to noise.
- Often requires smoothing before use.

---

## Canny Edge Detection

- Multi-stage edge detection algorithm.
- Uses Gaussian Blur before detecting edges.
- Produces thin and accurate edges.

### Advantages

- High accuracy
- Removes noise
- Produces clean boundaries

### Disadvantages

- Threshold values must be selected carefully.

---

# 📚 Purpose of Each Morphological Operation

## Erosion

- Shrinks white objects.
- Removes small white noise.

---

## Dilation

- Expands white objects.
- Connects broken edges.

---

## Opening

(Erosion → Dilation)

Purpose:

- Removes small white noise while preserving object shape.

---

## Closing

(Dilation → Erosion)

Purpose:

- Fills small gaps and holes.
- Connects broken document boundaries.

---

## Morphological Gradient

Purpose:

- Displays only the object boundary.

---

## Top Hat

Purpose:

- Highlights small bright objects.

---

## Black Hat

Purpose:

- Highlights small dark objects.

---

# ✅ Best Combination of Techniques

The following combination produced the best document boundary detection results:

- Grayscale Conversion
- Gaussian Blur (5×5)
- Canny Edge Detection (50, 150)
- Morphological Closing (5×5 Kernel)
- Largest Contour Detection
- Contour Approximation using approxPolyDP()

This pipeline successfully detected clear document boundaries in most document images.

---

# ⚠ Challenges Faced

During development, several challenges were encountered:

- Detecting non-document objects such as people or vehicles.
- Selecting suitable Canny threshold values.
- Broken document edges causing incomplete contours.
- Images with shadows and poor lighting.
- Background objects interfering with contour detection.
- Some images contained multiple large contours, making document selection difficult.

These challenges were reduced by applying Gaussian Blur, Morphological Closing, and selecting the largest contour.

---


# 👨‍💻 Author

**Muhammad Asad Ali**
