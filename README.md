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

Edit required settings in the `settings.py`

```python
# Video file
VIDEO_DIRPATH = ROOT / 'videos'             # EDIT: 1 (Required)
VIDEO_FILE_FULLNAME = 'truck.ts'            # EDIT: 2 (Required)

# Frame settings
REQUIRED_FRAME_RATE = 2                     # EDIT: 3
# Number of seconds for a frame. 2 means, 1 frame for 2 seconds

START_FROM_SECOND = 3                       # EDIT: 4
# start extraction of the frames after 3 seconds of the video is passed.

REQUIRED_IMAGE_FORMAT = 'png'               # EDIT: 5
REQUIRED_IMAGE_WIDTH = 480                  # EDIT: 6

# Output frames dirpath
OUTDIR = BASE_ROOT/'truck'                  # EDIT: 7 (Required)
```
