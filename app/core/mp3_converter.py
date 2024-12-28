import subprocess
from pathlib import Path
from app.core.utils import get_default_output_dir, get_mp3_file


def convert_to_mp3(url: str) -> Path:
    """
    Converts a YouTube video to an MP3 file and returns the file path.

    Args:
        url (str): The YouTube video URL.

    Returns:
        Path: Path to the converted MP3 file.
    """
    output_dir = Path(get_default_output_dir())
    output_dir.mkdir(parents=True, exist_ok=True)

    output_template = str(output_dir / '%(title)s.%(ext)s')

    command = [
        "yt-dlp",
        "--extract-audio",
        "--audio-format", "mp3",
        "-o", output_template,
        url
    ]

    # Run the command
    process_result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    if process_result.returncode != 0:
        raise RuntimeError(f"Error in yt-dlp: {process_result.stderr}")

    # Get the most recent MP3 file
    newest_mp3 = get_mp3_file(output_dir)
    if not newest_mp3:
        raise RuntimeError("Conversion succeeded, but the MP3 file could not be found.")

    return newest_mp3