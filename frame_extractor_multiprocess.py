from pathlib import Path
import time
import cv2
import imutils
import fire
import settings
from concurrent.futures import ProcessPoolExecutor


class FrameExtractor:
    def __init__(self, vid, out_dir, img_frmt='jpg', required_frame_rate=None, start_from_seconds=None, write_interval=10):
        self.vid = vid
        self.out_dir = out_dir
        self.img_frmt = img_frmt
        self.required_frame_rate = required_frame_rate or 1
        self.start_from_seconds = start_from_seconds or 0
        self.write_interval = write_interval

    def extract_frames(self):
        """Extract frames from a video."""
        count = 1
        orig_images = []
        resized_images = []

        self.out_dir.mkdir(exist_ok=True)

        # Get start time
        time_start = time.time()

        # Create dirs for orig and resized images inside the 'outdir'
        orig_file_dir = self.out_dir / 'orig_size'
        orig_file_dir.mkdir(exist_ok=True)
        resize_file_dir = self.out_dir / 'resize_file'
        resize_file_dir.mkdir(exist_ok=True)

        print("======================================")
        print(f"[OUT FILE DIRECTORY] - {self.out_dir}")
        vid_cap = cv2.VideoCapture(str(Path(self.vid)))
        # start from 1 if 'start_from_seconds' is not passed.
        sec = int(self.start_from_seconds)
        vid_cap.set(cv2.CAP_PROP_POS_MSEC, sec * 1000)
        vidname = self.vid.stem
        while (vid_cap.isOpened()):
            success, image = vid_cap.read()
            if success:
                try:
                    orig_images.append(image)
                    resized_images.append(imutils.resize(
                        image, width=settings.REQUIRED_IMAGE_WIDTH))

                    if count % self.write_interval == 0:
                        for i in range(len(orig_images)):
                            orig_file_location = f"{orig_file_dir}/{vidname}_{count - len(orig_images) + i + 1}.{self.img_frmt}"
                            resize_file_location = f"{resize_file_dir}/{vidname}_{count - len(orig_images) + i + 1}.{self.img_frmt}"
                            cv2.imwrite(orig_file_location, orig_images[i])
                            cv2.imwrite(resize_file_location,
                                        resized_images[i])
                        orig_images.clear()
                        resized_images.clear()

                        print(f"Done: {count}")
                except Exception as ex:
                    print("[ERROR CODE 1001]")
                    print(ex)
            else:
                time_end = time.time()
                for i in range(len(orig_images)):
                    orig_file_location = f"{orig_file_dir}/{vidname}_{count - len(orig_images) + i + 1}.{self.img_frmt}"
                    resize_file_location = f"{resize_file_dir}/{vidname}_{count - len(orig_images) + i + 1}.{self.img_frmt}"


if __name__ == '__main__':
    vid_dir = settings.VIDEO_DIRPATH
    out_dir = settings.OUTDIR
    required_frame_rate = settings.REQUIRED_FRAME_RATE
    start_from_seconds = settings.START_FROM_SECOND
    img_frmt = settings.REQUIRED_IMAGE_FORMAT

    if vid_dir.exists():
        for vid in vid_dir.iterdir():
            frame_extractor = FrameExtractor(
                vid, out_dir, img_frmt, required_frame_rate, start_from_seconds)
            frame_extractor.extract_frames()
    else:
        print(f"The specified path ({vid_dir}) does not exists!!!")
