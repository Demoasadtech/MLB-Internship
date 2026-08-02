"""
Document Image Enhancement Tool

    1. Auto-detects and corrects perspective (deskews a tilted document)
    2. Converts to grayscale
    3. Reduces noise
    4. Enhances brightness/contrast (CLAHE)
    5. Sharpens the result

"""

import cv2
import numpy as np
import gradio as gr


# PERSPECTIVE CORRECTION
SAMPLE_IMAGES = [       # sample image creation
    "Day15/input_images/d1.png",
    "Day15/input_images/document.png",
    "Day15/input_images/d2.png",
    "Day15/input_images/landscape.png",
    "Day15/input_images/d3.png",
    "Day15/input_images/object.png",
    "Day15/input_images/d4.png",
    "Day15/input_images/person.png",
    "Day15/input_images/d5.png",
    "Day15/input_images/vehicle.png"
    ]

def order_points(pts):
    """Sort 4 points into [top-left, top-right, bottom-right, bottom-left]."""
    rect = np.zeros((4, 2), dtype="float32")
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]      # top-left has smallest sum
    rect[2] = pts[np.argmax(s)]      # bottom-right has largest sum

    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]   # top-right has smallest difference
    rect[3] = pts[np.argmax(diff)]   # bottom-left has largest difference
    return rect


def four_point_transform(image, pts):
    """Warp the quadrilateral defined by pts into a straight, top-down view."""
    rect = order_points(pts)
    (tl, tr, br, bl) = rect
    width_a = np.linalg.norm(br - bl)
    width_b = np.linalg.norm(tr - tl)
    max_width = max(int(width_a), int(width_b))
    height_a = np.linalg.norm(tr - br)
    height_b = np.linalg.norm(tl - bl)
    max_height = max(int(height_a), int(height_b))

    if max_width == 0 or max_height == 0:
        return image  # degenerate case, bail out safely

    dst = np.array([
        [0, 0],
        [max_width - 1, 0],
        [max_width - 1, max_height - 1],
        [0, max_height - 1]], dtype="float32")

    matrix = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, matrix, (max_width, max_height))
    return warped


def find_document_contour(image):
    """Try to find a 4-point contour that looks like a document edge."""
    orig_h, orig_w = image.shape[:2]

    # Work on a resized copy for speed and reliable edge detection
    ratio = 500.0 / orig_h
    resized = cv2.resize(image, (int(orig_w * ratio), 500))
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 50, 150)
    edged = cv2.dilate(edged, None, iterations=1)
    edged = cv2.erode(edged, None, iterations=1)
    contours, _ = cv2.findContours(edged, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:5]

    for c in contours:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)

        # A document should be a big, roughly-rectangular (4 point) shape
        if len(approx) == 4 and cv2.contourArea(approx) > 0.2 * resized.shape[0] * resized.shape[1]:
            return approx.reshape(4, 2) / ratio  # scale back to original size

    return None


def correct_perspective(image, enable=True):
    """Detect the document's edges and warp it into a flat, top-down view."""
    if not enable:
        return image

    contour = find_document_contour(image)
    if contour is None:
        # No reliable 4-point document contour found  return original
        return image

    return four_point_transform(image, contour)



#GRAYSCALE / DENOISE / CONTRAST / SHARPEN
def to_grayscale(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)  # keep 3 channels for a consistent pipeline


def reduce_noise(image, strength=10):
    if strength <= 0:
        return image
    return cv2.fastNlMeansDenoisingColored(image, None, strength, strength, 7, 21)


def enhance_contrast_brightness(image, brightness=10, contrast_clip=2.0):
    """Brightness offset + CLAHE (adaptive contrast) applied on the luminance channel."""
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=contrast_clip, tileGridSize=(8, 8))
    l = clahe.apply(l)
    lab = cv2.merge((l, a, b))
    result = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

    if brightness != 0:
        result = cv2.convertScaleAbs(result, alpha=1.0, beta=brightness)

    return result


def sharpen_image(image, amount=1.0):
    """Unsharp mask: sharp = original + amount * (original - blurred)."""
    if amount <= 0:
        return image
    blurred = cv2.GaussianBlur(image, (0, 0), sigmaX=3)
    sharpened = cv2.addWeighted(image, 1 + amount, blurred, -amount, 0)
    return sharpened



# FULL PIPELINE
def enhance_document(
    image,
    do_perspective,
    do_grayscale,
    denoise_strength,
    brightness,
    contrast_clip,
    sharpen_amount,
):
    if image is None:
        return None

    # Gradio gives RGB numpy array -> convert to BGR for OpenCV
    img = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    img = correct_perspective(img, enable=do_perspective)
    img = reduce_noise(img, strength=denoise_strength)
    img = enhance_contrast_brightness(img, brightness=brightness, contrast_clip=contrast_clip)
    img = sharpen_image(img, amount=sharpen_amount)

    if do_grayscale:
        img = to_grayscale(img)

    # Convert back to RGB for Gradio display
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)



# GRADIO UI
with gr.Blocks(title="Document Image Enhancement Tool") as app:
    gr.Markdown(
        """
        # 📄 Document Image Enhancement Tool
        Upload a photo of a document (receipt, scan, ID card, printed page, etc.)
        and clean it up automatically: deskew → grayscale → denoise → contrast → sharpen.
        
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
            gr.Markdown("### Options")
            do_perspective = gr.Checkbox(value=True, label="Auto-correct perspective (deskew)")
            do_grayscale = gr.Checkbox(value=True, label="Convert to grayscale")

            denoise_strength = gr.Slider(0, 30, value=10, step=1, label="Noise Reduction Strength")
            brightness = gr.Slider(-100, 100, value=10, step=1, label="Brightness")
            contrast_clip = gr.Slider(0.5, 5.0, value=2.0, step=0.1, label="Contrast (CLAHE clip limit)")
            sharpen_amount = gr.Slider(0.0, 3.0, value=1.0, step=0.1, label="Sharpen Amount")

            run_btn = gr.Button("Enhance Document", variant="primary")
            clear_btn = gr.ClearButton(value="Clear",variant="secondary")
            
        with gr.Column(scale=1):
            output_image = gr.Image(label="Enhanced Document")

    run_btn.click(
        fn=enhance_document,
        inputs=[
            input_image,
            do_perspective,
            do_grayscale,
            denoise_strength,
            brightness,
            contrast_clip,
            sharpen_amount,
        ],
        outputs=output_image,
    )

    clear_btn.add([input_image,output_image])
    # Live preview whenever any control changes (optional convenience)
    for control in [do_perspective, do_grayscale, denoise_strength, brightness, contrast_clip, sharpen_amount]:
        control.change(
            fn=enhance_document,
            inputs=[
                input_image,
                do_perspective,
                do_grayscale,
                denoise_strength,
                brightness,
                contrast_clip,
                sharpen_amount,
            ],
            outputs=output_image,
        )

if __name__ == "__main__":
    app.launch()