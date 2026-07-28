'''Download the dataset in YOLO format.
Load a pre-trained YOLO model (YOLOv8 or YOLO11).
Run inference on the dataset or sample images.
Visualize the detection results.
Save the output images with bounding boxes.
Briefly analyze the model's predictions'''

from ultralytics import YOLO

# Load YOLO11 model
model = YOLO("yolo11n.pt")

# Run inference
results = model.predict(
    source="Day13/sample_images",
    save=True,
    project="Output",
    name="vehicles_dataset_results",
    conf=0.40
)

for result in results:  #print class name , confidence , and coordinates of bounding boxes and localization
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