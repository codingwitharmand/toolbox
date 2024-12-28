import os
from pathlib import Path
import platform

OUTPUT_DIR = "output/mp3"


def get_default_output_dir() -> str:
    """
    Returns the default downloads directory depending on the OS.
    """
    if platform.system() == "Windows":
        return os.path.join(os.environ["USERPROFILE"], "Downloads")
    else:
        return os.path.join(os.environ["HOME"], "Downloads")


def get_mp3_file(output_folder: Path) -> Path:
    """
    Fetches the newest MP3 file in the given folder.
    """
    newest_mp3 = None
    latest_mtime = 0

    for f in output_folder.glob("*.mp3"):
        mtime = f.stat().st_mtime
        if mtime > latest_mtime:
            latest_mtime = mtime
            newest_mp3 = f

    return newest_mp3