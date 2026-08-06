
import cv2
import numpy as np
import gradio as gr
import tempfile

SAMPLE_VIDEO = [       # sample video
    "Day18/input_video/14,August.mp4",
    "Day18/input_video/t1.mp4",
    "Day18/input_video/t2.mp4"
]

#function processing on frame one by one
def process_frame(frame, blur_ksize=5, canny_low=50, canny_high=150, show_mode="Edges Only"):
    
    #Grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Gaussian Blur (kernel size must be odd)
    k = int(blur_ksize)
    if k % 2 == 0:
        k += 1
    k = max(1, k)
    blurred = cv2.GaussianBlur(gray, (k, k), 0)

    #Canny Edge Detection
    edges = cv2.Canny(blurred, int(canny_low), int(canny_high))

    if show_mode == "Grayscale":
        out = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    elif show_mode == "Blurred":
        out = cv2.cvtColor(blurred, cv2.COLOR_GRAY2BGR)
    elif show_mode == "Side by Side":
        edges_bgr = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        out = np.hstack([frame, edges_bgr])
    else:  #Edges Only
        out = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    return out



#Process an uploaded video file
def process_video_file(video_path, blur_ksize, canny_low, canny_high, show_mode, progress=gr.Progress()):
    if video_path is None:
        raise gr.Error("Please upload the video")

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise gr.Error("video format is wrong, so that not opened on it")

    fps = cap.get(cv2.CAP_PROP_FPS) or 25.0
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) or 0
    out_width = width * 2 if show_mode == "Side by Side" else width
    out_path = tempfile.NamedTemporaryFile(suffix=".mp4", delete=False).name
    fourcc = cv2.VideoWriter_fourcc(*"avc1")
    writer = cv2.VideoWriter(out_path, fourcc, fps, (out_width, height))

    frame_idx = 0
    while True:
        bool_process, frame = cap.read()
        if not bool_process:
            break
        processed = process_frame(frame, blur_ksize, canny_low, canny_high, show_mode)
        writer.write(processed)
        frame_idx += 1
        if total_frames > 0:
            progress(frame_idx / total_frames, desc=f"Processing frame {frame_idx}/{total_frames}")

    cap.release()
    writer.release()

    return out_path, out_path  #preview player, download file



#Live webcame one frame in, one processed frame out streaming
def process_webcam_stream(frame, blur_ksize, canny_low, canny_high, show_mode):
    if frame is None:
        return None
    # gr.Image with webcam gives RGB numpy array — convert to BGR for OpenCV
    bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    processed = process_frame(bgr, blur_ksize, canny_low, canny_high, show_mode)
    rgb_out = cv2.cvtColor(processed, cv2.COLOR_BGR2RGB)
    return rgb_out



# UI
with gr.Blocks(title="Real-Time Video Edge Processor") as app:
    gr.Markdown(
         "# 🎥 Real-Time Video Processing Tool\n"
         "This application provides two processing modes:\n\n"
         "📁 **Video File:** Upload a recorded video, process every frame, preview the output, and download the processed video.\n\n"
         "📷 **Live Webcam:** Capture and process your webcam feed in real time with instant visual results."
    )

    with gr.Tab("📁 Video File"):
        with gr.Row():
            with gr.Column():
                video_input = gr.Video(label="Upload Video")
                if SAMPLE_VIDEO:
                                gr.Examples(
                                examples=SAMPLE_VIDEO,
                                inputs=video_input,
                                label="Or try a sample image",
                                 )
                blur_1 = gr.Slider(1, 31, value=5, step=2, label="Gaussian Blur Kernel Size")
                low_1 = gr.Slider(0, 255, value=50, step=1, label="Canny Lower Threshold")
                high_1 = gr.Slider(0, 255, value=150, step=1, label="Canny Upper Threshold")
                mode_1 = gr.Radio(
                    ["Edges Only", "Grayscale", "Blurred", "Side by Side"],
                    value="Edges Only",
                    label="Display Mode",
                )
                run_btn = gr.Button("▶ Process Video", variant="primary")
                clear_btn = gr.ClearButton(value="Clear",variant="secondary")
            with gr.Column():
                video_preview = gr.Video(label="Processed Video (Preview)")
                video_download = gr.File(label="Download Processed Video")

        run_btn.click(
            fn=process_video_file,
            inputs=[video_input, blur_1, low_1, high_1, mode_1],
            outputs=[video_preview, video_download],
        )
    clear_btn.add([video_input,video_download,video_preview])
    with gr.Tab("📷 Webcam (Live)"):
        with gr.Row():
            with gr.Column():
                webcam_input = gr.Image(sources=["webcam"], streaming=True, label="Webcam Input")
                blur_2 = gr.Slider(1, 31, value=5, step=2, label="Gaussian Blur Kernel Size")
                low_2 = gr.Slider(0, 255, value=50, step=1, label="Canny Lower Threshold")
                high_2 = gr.Slider(0, 255, value=150, step=1, label="Canny Upper Threshold")
                mode_2 = gr.Radio(
                    ["Edges Only", "Grayscale", "Blurred", "Side by Side"],
                    value="Edges Only",
                    label="Display Mode",
                )
                clear_btn = gr.ClearButton(value="Clear",variant="secondary")
            with gr.Column():
                webcam_output = gr.Image(label="Processed Output", streaming=True)

        webcam_input.stream(
            fn=process_webcam_stream,
            inputs=[webcam_input, blur_2, low_2, high_2, mode_2],
            outputs=webcam_output,
            time_limit=60,
            stream_every=0.1,
        )
    clear_btn.add([webcam_input,webcam_output])
if __name__ == "__main__":
    app.launch()