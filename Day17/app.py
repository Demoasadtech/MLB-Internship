import cv2
import numpy as np
import gradio as gr

SAMPLE_IMAGES = [       # sample image creation
    "Day17/input_images/p1.png",
    "Day17/input_images/d4.png",
    "Day17/input_images/object.png",
    "Day17/input_images/p3.png",
    "Day17/input_images/p5.png",
    ]
def detect_shapes(image):

    try:

        # Check image
        if image is None:
            raise ValueError("Please upload an image.")

        # RGB to BGR
        img = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        _, thresh = cv2.threshold(
            gray,
            127,
            255,
            cv2.THRESH_BINARY_INV
        )

        contours, _ = cv2.findContours(
            thresh,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        info = []

        for cnt in contours:

            area = cv2.contourArea(cnt)

            if area < 100:
                continue

            perimeter = cv2.arcLength(cnt, True)

            epsilon = 0.02 * perimeter

            approx = cv2.approxPolyDP(
                cnt,
                epsilon,
                True
            )

            corners = len(approx)

            x, y, w, h = cv2.boundingRect(approx)

            if corners == 3:
                shape = "Triangle"

            elif corners == 4:

                ratio = w / float(h)

                if 0.95 <= ratio <= 1.05:
                    shape = "Square"
                else:
                    shape = "Rectangle"

            elif corners >= 8:
                shape = "Circle"

            else:
                shape = "Polygon"

            # Draw Contour
            cv2.drawContours(
                img,
                [approx],
                -1,
                (0, 255, 0),
                2
            )

            # Draw Bounding Box
            cv2.rectangle(
                img,
                (x, y),
                (x + w, y + h),
                (0, 255, 255),
                2
            )

            # Shape Label
            cv2.putText(
                img,
                shape,
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255, 0, 0),
                2
            )

            info.append(
                f"{shape} | Area: {area:.2f} | Perimeter: {perimeter:.2f}"
            )

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        if len(info) == 0:
            info.append("No valid shapes detected.")

        return img, "\n".join(info)

    except ValueError as e:
        return None, f"Input Error: {e}"

    except cv2.error as e:
        return None, f"OpenCV Error:\n{e}"

    except Exception as e:
        return None, f"Unexpected Error:\n{e}"


# GRADIO UI
with gr.Blocks(title="Document Image Enhancement Tool") as app:
    gr.Markdown(
        """
        # Shape Detection Tool
        Upload an image containing geometric shapes.This application can detect:🔺 Triangle,◼️ Square, ▭ Rectangle, ⚪ Circle, ⬟ Polygon
        
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
            status = gr.Textbox(label="Shape Information",interactive=False)

    run_btn.click(
        fn=detect_shapes,
        inputs=input_image,
        outputs=[output_image, status] 
    )

    clear_btn.add([input_image,output_image,status])

if __name__ == "__main__":
    app.launch()