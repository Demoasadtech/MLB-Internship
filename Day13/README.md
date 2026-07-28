# Day-13: Object Detection using YOLO11

## Project Overview

This project demonstrates Object Detection using the pre-trained YOLO11 model from the Ultralytics library. The model is used to detect different types of vehicles in images without training a new model. A simple Gradio application is also developed to allow users to upload an image and view the detected objects with bounding boxes.

---

## What is Object Detection?

Object Detection is a Computer Vision task that identifies and locates one or more objects in an image. It not only predicts the object's class but also draws a bounding box around each detected object and provides a confidence score.

---

## How is it different from Image Classification?

Image Classification predicts only the category of an entire image. It does not identify the location of objects.

Object Detection, on the other hand, detects multiple objects in an image, identifies their classes, and provides their exact locations using bounding boxes.

---

## What is YOLO?

YOLO (You Only Look Once) is a fast and efficient real-time object detection algorithm. It processes the entire image in a single forward pass and predicts object classes, bounding boxes, and confidence scores at the same time. Because of its speed and accuracy, YOLO is widely used in real-world applications such as autonomous vehicles, traffic monitoring, surveillance, and robotics.

---

## Which Dataset Did You Use?

I used a **Vehicle Detection Dataset** downloaded in **YOLO format**. The images contain different types of vehicles such as cars, buses, trucks, and motorcycles.

---

## What Objects Were Detected?

The pre-trained YOLO11 model successfully detected:

- Car
- Bus
- Truck
- Motorcycle
- Person

Each detected object was displayed with a bounding box, class label, and confidence score.

---

## Observations About the Detection Results

- The model detected most vehicles accurately.
- Larger and clearer vehicles received higher confidence scores.
- Small or partially hidden vehicles sometimes had lower confidence scores.
- Since vehicle classes are already included in the COCO dataset, the pre-trained model performed well without additional training.
- YOLO provided fast detection, making it suitable for real-time applications.

---

## How My Gradio App Works

The Gradio application provides a simple interface for object detection.

1. The user uploads a vehicle image or selects one of the sample images.
2. The image is sent to the pre-trained YOLO11 model.
3. The model performs object detection and predicts the detected vehicles.
4. Bounding boxes are drawn around the detected objects.
5. The output image and a status message showing the number of detected objects are displayed.
6. A **Clear** button allows the user to reset the application for another prediction.

---

## Technologies Used

- Python
- Ultralytics YOLO11
- Gradio
- NumPy

---

# 📂 Project Files

```
Day-13/
│
├── Sample_images  (Folder)
├── Vehicle dataset ( yolo format)
├── README.md
├── Object Detection Script
├── YOLO Practice Script
├── app Script
└── requirements.txt
```

---

## Conclusion

This project helped me understand the fundamentals of Object Detection using YOLO11. I learned how to perform inference with a pre-trained model, interpret bounding boxes, confidence scores, and class labels, and develop a simple Gradio application for real-time object detection.

---

# 👨‍💻 Author

**Muhammad Asad Ali**