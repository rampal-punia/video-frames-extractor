import os
import time
import cv2
import imutils

import settings_vidframe as settings


def extract_images_from_video(vid_name,
                              vid_cap,
                              out_dirname,
                              img_frmt='jpg',
                              required_frame_rate=None,
                              start_from_seconds=None
                              ):
    count = 0
    time_start = time.time()

    if start_from_seconds:
        sec = int(start_from_seconds)
    else:
        sec = 1

    if required_frame_rate:
        framerate = float(required_frame_rate)
    else:
        framerate = 1
    print("======================================")
    print(f"[OUT FILE DIRECTORY] - {out_dirname}")
    while (vid_cap.isOpened()):
        vid_cap.set(cv2.CAP_PROP_POS_MSEC, sec*1000)
        success, image = vid_cap.read()
        if success:
            try:
                # save frames
                orig_file_dir = os.path.join(out_dirname, 'orig_file')
                resize_file_dir = os.path.join(out_dirname, 'resize_file')
                if not (os.path.exists(orig_file_dir) and os.path.exists(resize_file_dir)):
                    os.makedirs(orig_file_dir)
                    os.makedirs(resize_file_dir)

                orig_file_location = f"{orig_file_dir}/{vid_name}_{count}.{img_frmt}"
                resize_file_location = f"{resize_file_dir}/{vid_name}_{count}.{img_frmt}"

                cv2.imwrite(orig_file_location, image)
                img = cv2.imread(orig_file_location)
                img = imutils.resize(img, width=settings.REQUIRED_IMAGE_WIDTH)
                cv2.imwrite(resize_file_location, img)
                count += 1
                sec = sec + framerate
                sec = round(sec, 2)
            except Exception as ex:
                print("[ERROR CODE 1001]")
                print(ex)
        elif cv2.waitKey(25) & 0xFF == ord('q'):
            # Log the time again
            time_end = time.time()
            # Release the feed
            vid_cap.release()
            # Print stats
            print("Done extracting frames.\n%d frames extracted" % count)
            print("It took %d seconds for conversion." % (time_end-time_start))
            break
        else:
            time_end = time.time()
            print("Done extracting frames.\n%d frames extracted" % count)
            print(f"It took {time_end-time_start:.2f} seconds for conversion.")
            vid_cap.release()
            break


vid_path = settings.VIDEO_FILE_PATH
vid_name = settings.VIDNAME_WITHOUT_EXT
required_frame_rate = settings.REQUIRED_FRAME_RATE
start_from_seconds = settings.START_FROM_SECOND
out_dirname = settings.OUTDIR
img_frmt = settings.REQUIRED_IMAGE_FORMAT

if os.path.exists(vid_path):
    vid_cap = cv2.VideoCapture(vid_path)
    frames = int(vid_cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    print(f"[TOTAL FRAMES] - {frames}")
    fps = int(vid_cap.get(cv2.CAP_PROP_FPS))
    print(f"[FRAMES PER SECOND] - {fps}")
    seconds = int(frames/fps)
    print(f"[VIDEO LENGTH] - {seconds} seconds")

    extract_images_from_video(vid_name,
                              vid_cap,
                              out_dirname,
                              img_frmt,
                              required_frame_rate,
                              start_from_seconds
                              )
else:
    print(f"The specified path ({vid_path}) does not exists!!!")
