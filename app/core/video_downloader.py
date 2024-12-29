import subprocess
from pathlib import Path

from app.core.utils import get_default_output_dir


def download_video(url: str, format: str = "mp4", quality: str = "medium") -> Path:
    quality_levels = {
        "low": "worst",
        "medium": "best[height<=720]",
        "high": "best[height<=1080]",
        "best": "best"
    }

    if quality not in quality_levels:
        raise ValueError(f"Invalid quality: '{quality}'. Use one of {', '.join(quality_levels.keys())}.")

    output_dir = Path(get_default_output_dir())
    output_dir.mkdir(parents=True, exist_ok=True)

    output_template = str(output_dir / '%(title)s.%(ext)s')

    command = [
        "yt-dlp",
        "-f", quality_levels[quality],
        "-o", output_template,
        url
    ]

    process_result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    if process_result.returncode != 0:
        raise RuntimeError(f"Error in yt-dlp: {process_result.stderr}")

    video_files = list(output_dir.glob(f"*.{format}"))
    if not video_files:
        raise RuntimeError("Download succeeded, but the video file could not be found.")

    return max(video_files, key=lambda f: f.stat().st_mtime)