'''
Create object dection app ( model : yolo11n) using
gradio library used to find object on images
and give bounding box , Confidence'''

import gradio as gr
import numpy as np
from ultralytics import YOLO
# Load YOLO model (loaded once when the app starts)
try:
    model = YOLO("yolo11n.pt")
except Exception as e:
    model = None
    print(f"[ERROR] Could not load YOLO model: {e}")
# Sample images
SAMPLE_IMAGES = [
    "sample_images/f1.png",
    "sample_images/f2.png",
    "sample_images/f3.png",
    "sample_images/f4.png",
    "sample_images/f5.png"

    ]

def detect_vehicle(image):
   
    try:
        # 1. No image provided
        if image is None:
            return None, "⚠️ Please upload an image before proceeding."
        # 2. Validate that it's actually a proper image (numpy array with 3 dims, RGB/Gray)
        if not isinstance(image, np.ndarray):
            return None, "❌ Invalid file. Please upload a valid image."
        if image.ndim not in (2, 3) or image.size == 0:
            return None, "❌ Invalid file. Please upload a valid image."
        # 3. Model failed to load
        if model is None:
            return None, "❌ Detection model failed to load. Please contact the app administrator."
        # 4. Run inference
        results = model.predict(source=image, conf=0.40, verbose=False)
        if not results or len(results) == 0:
            return None, "⚠️ No results returned. Please try a different image."
        output_image = results[0].plot()
        num_detections = len(results[0].boxes) if results[0].boxes is not None else 0
        if num_detections == 0:
            return output_image, "✅ Processing completed successfully. No object were detected in this image."
        return output_image, f"✅ Success! {num_detections} object(s) detected."
    except Exception as e:
        # Never let a raw traceback reach the UI
        return None, f"❌ Something went wrong while processing the image: {str(e)}"

# UI
with gr.Blocks(title="Vehicle Detection using YOLO11", theme=gr.themes.Soft()) as app:

    gr.Markdown(
        """
        # 📷🤖🔍 Object Detection using YOLO11n
        Upload an image and detect vehicles (cars, buses, trucks, motorbikes, etc.) using a pre-trained YOLO11n model.

        **Developed by Muhammad Asad Ali**
        """
    )

    with gr.Row():
        with gr.Column(scale=1):
            image_input = gr.Image(type="numpy", label="Upload Image")

            if SAMPLE_IMAGES:
                gr.Examples(
                    examples=SAMPLE_IMAGES,
                    inputs=image_input,
                    label="Or try a sample image",
                )

            with gr.Row():
                clear_btn = gr.ClearButton(value="Clear")
                submit_btn = gr.Button("Submit", variant="primary")

        with gr.Column(scale=1):
            image_output = gr.Image(type="numpy", label="Detection Result")
            status_output = gr.Textbox(label="Status", interactive=False)

    clear_btn.add([image_input, image_output, status_output])

    submit_btn.click(
        fn=detect_vehicle,
        inputs=image_input,
        outputs=[image_output, status_output],
    )

if __name__ == "__main__":
    app.launch()