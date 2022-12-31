# Video Frames Extractor

For the annotation of the images, sometimes we need to extract frames from a video. To train a model first we need a dataset of the images of the object-of-interest. And many times we may have the data in the form of video.

This simple code help to extract images from the video.

## Requirements

```bash
# Dependencies
pip install opencv-python
pip install imutils

# Videos
# Keep the required video in the 'videos' folder. Or change
# the path inside settings file.
```

## Settings

```python
# Video file
VIDEO_DIRPATH = ROOT / 'videos'         # EDIT: 1
VIDEO_FILE_FULLNAME = 'vid_1.mp4'        # EDIT: 2

# Frame settings
REQUIRED_FRAME_RATE = 2               # EDIT: 3
START_FROM_SECOND = 1                   # EDIT: 4
REQUIRED_IMAGE_FORMAT = 'png'          # EDIT: 5
REQUIRED_IMAGE_WIDTH = 480

# Output frames dirpath
OUTDIR = BASE_ROOT/'vid_1'             # EDIT: 6
```
