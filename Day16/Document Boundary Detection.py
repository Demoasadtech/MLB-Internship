import cv2
import numpy as np
import gradio as gr

# Document Detection Function
SAMPLE_IMAGES = [       # sample image creation
    "Day16/input_images/document.png",
    "Day16/input_images/d2.png",
    "Day16/input_images/object.png",
    "Day16/input_images/d4.png",
    "Day16/input_images/person.png",
    "Day16/input_images/d5.png",
    "Day16/input_images/vehicle.png"
    ]
def detect_document(image):

    try:

        # Check if image is uploaded
        if image is None:
            raise ValueError("Please upload a document image.")

        # RGB -> BGR
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Create copy
        output = image.copy()

        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Gaussian Blur
        blur = cv2.GaussianBlur(gray, (5,5), 0)

        # Canny Edge Detection
        edges = cv2.Canny(blur, 50, 150)

        # Morphological Closing
        kernel = np.ones((5,5), np.uint8)

        edges = cv2.morphologyEx(
            edges,
            cv2.MORPH_CLOSE,
            kernel
        )

        # Find Contours
        contours, _ = cv2.findContours(
            edges,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        if len(contours) == 0:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            return image, "❌ No Document Boundary Found."

        # Largest Contour
        largest = max(contours, key=cv2.contourArea)

        # Approximate Contour
        epsilon = 0.02 * cv2.arcLength(largest, True)

        approx = cv2.approxPolyDP(
            largest,
            epsilon,
            True
        )

        # Draw Boundary
        cv2.drawContours(
            output,
            [approx],
            -1,
            (0,255,0),
            3
        )

        # Convert back to RGB
        output = cv2.cvtColor(
            output,
            cv2.COLOR_BGR2RGB
        )

        return output, "✅ Document Boundary Detected Successfully."


    except ValueError as e:
        raise gr.Error(str(e))

    except cv2.error:
        return None, "❌ OpenCV failed to process the image."

    except FileNotFoundError:
        return None, "❌ Sample image not found."

    except Exception as e:
        return None, f"❌ Error: {e}"


# GRADIO UI
with gr.Blocks(title="Document Image Enhancement Tool") as app:
    gr.Markdown(
        """
        # 📄Document Boundary Detection Tool
        Upload a document image (receipt, invoice, scanned page, ID card, or printed paper).  
        This application automatically detects the document boundary.
        
        **Developed by Muhammad Asad Ali**
        """
    )
    with gr.Row():
        with gr.Column(scale=1):
            input_image = gr.Image(label="Input Document Image", type="numpy")
            if SAMPLE_IMAGES:
                gr.Examples(
                examples=SAMPLE_IMAGES,
                inputs=input_image,
                label="Or try a sample image",
                 )
            run_btn = gr.Button("Image Proceed", variant="primary")
            clear_btn = gr.ClearButton(value="Clear",variant="secondary")
            
        with gr.Column(scale=1):
            output_image = gr.Image(label="Detected Object")
            status = gr.Textbox(label="Detection Status",interactive=False)

    run_btn.click(
        fn=detect_document,
        inputs=input_image,
        outputs=[output_image, status] 
    )

    clear_btn.add([input_image,output_image,status])

if __name__ == "__main__":
    app.launch()