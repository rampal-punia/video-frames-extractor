# Video Frames Extractor

## Table of Contents

- [Overview](https://github.com/CodingMantras/video-frames-extractor#overview)
- [Why this app?](https://github.com/CodingMantras/video-frames-extractor#why-this-app)
- [Features](https://github.com/CodingMantras/video-frames-extractor#features)
- [Installation](https://github.com/CodingMantras/video-frames-extractor#installation)
- [Example](https://github.com/CodingMantras/video-frames-extractor#example)
- [Configuration](https://github.com/CodingMantras/video-frames-extractor#configuration)
- [Feedback](https://github.com/CodingMantras/video-frames-extractor#feedback)
- [License](https://github.com/CodingMantras/video-frames-extractor#license)

## Overview

The Video Frame Extractor is a Python script that allows you to extract frames from a video file and save them as individual image files in two different directories: one for the original size frames and one for the resized frames. The script uses OpenCV and imutils Python packages for image processing and Fire Python package for a simplified command-line interface.

This script allows you to extract frames from videos at a specified rate. By specifying the desired interval (in seconds) between extracted frames, you can quickly generate a large dataset of images for object detection, image classification, or other computer vision tasks.

## Why this app?

For image annotation, it's often necessary to extract frames from videos. This application makes it easy to generate a large dataset of images for training object detection or image classification models, even if your data is initially in the form of videos.

By automating the frame extraction process for iterating over all the video files inside a directory, this app saves you time and effort compared to manually extracting frames from each video file.

Hope you find the Video Frame Extractor useful for your computer vision projects!

## Features

To use the Video Frame Extractor, you need to run the `frame_extractor.py` Python script with the following arguments:

- `vid_dir`: the path to the directory containing the video file(s) you want to extract frames from.
- `out_dir`: the path to the directory where you want to save the extracted frames.
- `img_frmt` (optional): the image format to save the extracted frames in. Default is **jpg**.
- `required_frame_rate` (optional): the number of frames to extract per second. Default is **1**.
- `start_from_seconds` (optional): the number of seconds from which to start extracting frames. Default is **0**.

The app will extract frames from all videos in the specified directory and save them to the output directory.

Instead of passing the arguments every time you run this app you can add these arguments inside the settings.py file. [settings](https://github.com/CodingMantras/video-frames-extractor#edit-the-settings)

## Installation

To use the Video Frame Extractor, you need to have Python 3 and the following Python packages installed:

- OpenCV
- imutils
- Fire

You can install these packages using pip, by running the following command in your terminal:

```bash
pip install opencv-python imutils fire
```

### Help

```python
python frame_extractor.py --help
```

### Run

```python
python frame_extractor.py --vid_dir=[vid_dir] --out_dir=[out_dir] --img_frmt=[img_frmt] --required_frame_rate=[required_frame_rate] --start_from_seconds=[start_from_seconds]
```

## Example

Suppose you have a video file called my_video.mp4 located in the /path/to/video directory, and you want to extract frames from it and save them in the /path/to/output directory, with a frame rate of 2 frames per second and starting from 10 seconds into the video. You can run the following command:

```python
python frame_extractor.py --vid_dir=/path/to/video --out_dir=/path/to/output --required_frame_rate=2 --start_from_seconds=10
```

The script will extract frames from my_video.mp4, save the original size frames in /path/to/output/orig_size_frames directory and the resized frames in /path/to/output/re_size_frames directory. The extracted frames will be saved in JPEG format, with a filename of the form my_video_1.jpg, my_video_2.jpg, and so on.

## Configuration

Alternatively you can edit the settings.py file and the `frame_extractor.py` will accept the arguments from here.

For example:

### Edit the Settings

Edit required settings in the `settings.py`

```python
# Video file
VIDEO_DIRPATH = ROOT / 'videos'             # EDIT: 1 (Required)

# Frame settings
REQUIRED_FRAME_RATE = 2                 # EDIT: 2
# Number of seconds for a frame. For example: 0.5 means, 1 frame after 0.5 seconds pass

START_FROM_SECOND = 1                      # EDIT: 3
# For example: 2 means, start extraction of the frames after 2 seconds of the video is passed.

REQUIRED_IMAGE_FORMAT = 'jpg'               # EDIT: 4
REQUIRED_IMAGE_WIDTH = 720                  # EDIT: 5

# Output frames dirpath
OUTDIR = BASE_ROOT/'skyscraper'             # EDIT: 6 (Required)
```

## Feedback

If you encounter any issues with the app or have any feedback or suggestions for improvement [raise an issue](https://github.com/CodingMantras/video-frames-extractor/issues)

## License

The Video Frame Extractor is licensed under the MIT License. See the [LICENSE](https://github.com/CodingMantras/video-frames-extractor/blob/master/LICENSE) file for details.
