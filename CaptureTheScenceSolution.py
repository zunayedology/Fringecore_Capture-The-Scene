import cv2

filename = 'video.mp4'
target_resolution = (3090, 1205)
output_file = f'output.jpg'
frame_step = 10
stitching_mode = cv2.Stitcher_PANORAMA

cap = cv2.VideoCapture(filename)
n_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

print(f"Video Information: Frames={n_frames}, Resolution={width}x{height}, FPS={fps}")

stitcher = cv2.Stitcher.create(stitching_mode)

frames = []
success, frame = cap.read()
count = 0

while success:
    print(f"Processing frame: {count}/{n_frames}")

    frames.append(frame)
    count += frame_step
    cap.set(cv2.CAP_PROP_POS_FRAMES, count)
    success, frame = cap.read()

cap.release()

print("Stitching frames...")
status, panorama = stitcher.stitch(frames)

if status == cv2.Stitcher_OK:
    print("Stitching completed successfully.")

    panorama_resized = cv2.resize(panorama, target_resolution)
    cv2.imwrite(output_file, panorama_resized)

    print(f"Panorama saved as {output_file}")

else:
    print(f"Stitching failed with status code: {status}")
