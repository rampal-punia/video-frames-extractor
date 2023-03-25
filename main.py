from pathlib import Path
import time
import fire

import frame_extractor
import settings


def main(vid_dir: str = settings.VIDEO_DIRPATH,
         out_dir: str = settings.OUTDIR,
         img_frmt: str = settings.REQUIRED_IMAGE_FORMAT,
         required_frame_rate: int = settings.REQUIRED_FRAME_RATE,
         start_from_seconds: int = settings.START_FROM_SECOND,
         img_width: int = settings.REQUIRED_IMAGE_WIDTH,
         verbose=True,
         ):
    """Extract frames from videos and save them as images.

    Args:
        vid_dir (str, optional): Path of video file. Defaults to str(settings.VIDEO_DIRPATH).
        out_dir (str, optional): Path of the output file. Defaults to str(settings.OUTDIR).
        img_frmt (str, optional): Type of output image. Defaults to settings.REQUIRED_IMAGE_FORMAT.
        required_frame_rate (int, optional): Interval between extracted frames. Defaults to int(settings.REQUIRED_FRAME_RATE).
        start_from_seconds (int, optional): To start extraction of frame from second. Defaults to int(settings.START_FROM_SECOND).
        img_width (int, optional): required image width. Defaults to int(settings.REQUIRED_IMAGE_WIDTH).
        verbose (bool, optional): Is the texts information inside output terminal required. Defaults to True.
    """

    vid_dir_path = Path(vid_dir)
    out_dir = Path(out_dir)

    # width and height (considering 16:9 format)
    img_width = img_width, int((img_width*9)/16)
    if vid_dir_path.exists():
        time_start = time.time()
        for vid in vid_dir_path.iterdir():
            frm_ext = frame_extractor.FrameExtractor(vid,
                                                     out_dir,
                                                     img_frmt,
                                                     required_frame_rate,
                                                     start_from_seconds,
                                                     img_width,
                                                     verbose)
            frm_ext.extract_frames()
        time_end = time.time()
        if verbose:
            print(
                f"It took {time_end-time_start:.2f} seconds for conversion.")
    else:
        print(f"The specified path ({vid_dir}) does not exist!")


if __name__ == '__main__':
    fire.Fire(main)
