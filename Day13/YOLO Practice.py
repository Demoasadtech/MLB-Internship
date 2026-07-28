'''
Coding Practice

Practice 1

Install the Ultralytics YOLO package and explore its basic usage.

Load a pre-trained YOLO model.
Perform object detection on:

  
An image
Multiple images
Save the prediction results.

Practice 2

Test the model on your own images.
Observe:

  
Detected objects
Confidence scores
Bounding boxes'''

from ultralytics import YOLO
# Load YOLO11 model
model = YOLO("yolo11n.pt")
# Run inference
results = model.predict(
    source="Day13/sample_images",
    save=True,
    project="Output",
    name="sample_images_results",
    conf=0.40
)
for result in results:    #print class name , confidence , and coordinates of bounding boxes and localization
    print(f"\nImage: {result.path}")
    for box in result.boxes:
        class_id = int(box.cls[0])
        class_name = model.names[class_id]
        confidence = float(box.conf[0])
        x1, y1, x2, y2 = box.xyxy[0].tolist()
        print(f"Class       : {class_name}")
        print(f"Confidence  : {confidence:.2f}")
        print(f"Coordinates : ({x1:.2f}, {y1:.2f}, {x2:.2f}, {y2:.2f})")
        print("-" * 40)
