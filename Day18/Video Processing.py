import cv2
video= cv2.VideoCapture("Day18/output_video/out_grayscale_video.mp4")
total_frame=video.get(cv2.CAP_PROP_FRAME_COUNT)
fps=video.get(cv2.CAP_PROP_FPS)
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("Duration:", total_frame/fps)
print("FPS:", fps)
print("Width:", width)
print("Height:", height)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
writer = cv2.VideoWriter(
    "Day18/output_video/out_grayscale_video.mp4",
    fourcc,
    fps,
    (width, height),
    False,
)
while True:

    success, frame = video.read()

    if not success:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #writer.write(gray)
    cv2.imshow("Video", frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

video.release()
#writer.release()
cv2.destroyAllWindows()