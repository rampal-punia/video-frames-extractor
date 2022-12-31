import os
import sys
from pathlib import Path

# Root folder
FILE = Path(__file__).resolve()
BASE_ROOT = FILE.parents[0]      # directory of the settings file (ROOT)
if str(BASE_ROOT) not in sys.path:
    sys.path.append(str(BASE_ROOT))
ROOT = Path(os.path.relpath(BASE_ROOT, Path.cwd()))

#############################
### Edit these settings ###
#############################
# Video file
VIDEO_DIRPATH = ROOT / 'videos'             # EDIT: 1 (Required)
VIDEO_FILE_FULLNAME = 'vid_2.mp4'            # EDIT: 2 (Required)

# Frame settings
REQUIRED_FRAME_RATE = 0.5                    # EDIT: 3
# Number of seconds for a frame. For example: 0.5 means, 1 frame after 0.5 seconds pass

START_FROM_SECOND = 1                      # EDIT: 4
# For example: 2 means, start extraction of the frames after 2 seconds of the video is passed.

REQUIRED_IMAGE_FORMAT = 'png'               # EDIT: 5
REQUIRED_IMAGE_WIDTH = 480                  # EDIT: 6

# Output frames dirpath
OUTDIR = BASE_ROOT/'vid_2'                  # EDIT: 7 (Required)

### END EDIT ###

VIDNAME_WITHOUT_EXT = os.path.splitext(VIDEO_FILE_FULLNAME)[0]
VIDEO_FILE_PATH = os.path.join(VIDEO_DIRPATH, VIDEO_FILE_FULLNAME)
if not os.path.exists(OUTDIR):
    os.makedirs(OUTDIR)
