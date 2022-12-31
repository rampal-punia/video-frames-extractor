import os
import sys
from pathlib import Path

# Root folder
FILE = Path(__file__).resolve()
BASE_ROOT = FILE.parents[0]      # directory of the settings file (ROOT)
if str(BASE_ROOT) not in sys.path:
    sys.path.append(str(BASE_ROOT))
ROOT = Path(os.path.relpath(BASE_ROOT, Path.cwd()))

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

VIDNAME_WITHOUT_EXT = os.path.splitext(VIDEO_FILE_FULLNAME)[0]
VIDEO_FILE_PATH = os.path.join(VIDEO_DIRPATH, VIDEO_FILE_FULLNAME)
if not os.path.exists(OUTDIR):
    os.makedirs(OUTDIR)
