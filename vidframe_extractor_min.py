import os
import cv2


vid_path = "videos/skyscraper.mp4"
outdir = "videos/"
frame_count = 0

vid_cap = cv2.VideoCapture(vid_path)

while (vid_cap.isOpened()):
    vid_cap.set(cv2.CAP_PROP_POS_MSEC, 1000)
    success, image = vid_cap.read()
    if success:
        filename = f"{outdir}/image_{frame_count}.png"
        # write image to the outdir
        cv2.imwrite(filename, image)
    else:
        vid_cap.release()

    frame_count += 1
