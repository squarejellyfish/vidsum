import cv2
import os
from math import floor

ss = 0
folders = [f for f in os.listdir() if os.path.isdir(f)]
for folder in folders:
    vids = [
        f"{folder}/{v}" for v in os.listdir(folder) if os.path.splitext(v)[1] == ".mp4"]
    s = 0
    for vid in vids:
        video = cv2.VideoCapture(vid)
        frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)
        fps = video.get(cv2.CAP_PROP_FPS)
        duration = frame_count / fps
        s += floor(duration)
    print(f"{folder}: {s} s")
    ss += s

print(f"sum of all: {ss} s")
