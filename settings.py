import sys
from pathlib import Path

# Get the absolute path of the current file and resolve any symbolic links
FILE = Path(__file__).resolve()

# Get the parent directory of the current file, which is the root folder of the project
BASE_ROOT = FILE.parents[0]

# Check if the root folder is already in the system path, and add it if it's not
if str(BASE_ROOT) not in sys.path:
    sys.path.append(str(BASE_ROOT))

# Get the relative path from the root folder to the current working directory
ROOT = Path(Path.relative_to(BASE_ROOT, Path.cwd()))


#############################
### Edit these settings ###
#############################
# Video file
VIDEO_DIRPATH = ROOT / 'videos'             # EDIT: 1 (Required)

# Frame settings
REQUIRED_FRAME_RATE = 8                 # EDIT: 2
# Number of seconds for a frame. For example: 0.5 means, 1 frame after 0.5 seconds pass

START_FROM_SECOND = 1                      # EDIT: 3
# For example: 2 means, start extraction of the frames after 2 seconds of the video is passed.

REQUIRED_IMAGE_FORMAT = 'jpg'               # EDIT: 4
REQUIRED_IMAGE_WIDTH = 720                  # EDIT: 5

# Output frames dirpath
OUTDIR = BASE_ROOT/'skyscraper_1'             # EDIT: 6 (Required)

### END EDIT ###
