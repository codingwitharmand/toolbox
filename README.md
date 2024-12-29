# Toolbox API
Toolbox API is a FastAPI-based project that provides useful utilities for various tasks. The current version includes functionality for:
- **YouTube to MP3 converter**: Convert YouTube videos into downloadable MP3 audio files.
- **YouTube video downloader**: Download YouTube videos in multiple formats and quality options.

The API is designed to be extensible, allowing the addition of future tools and utilities in a modular structure.
## Features
- **YouTube MP3 Converter**:
    - Convert YouTube videos to MP3 formats for offline listening.
    - Simple API design for ease of use.

- **YouTube Video Downloader**:
    - Download YouTube videos in different formats (`mp4`, `webm`, etc.).
    - Supports customizable quality levels (e.g., low, medium, high, best).

- Future utilities (e.g., file format converters, text extractors) can be added seamlessly.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technical Details](#technical-details)
- [Testing](#testing)
- [Future Plans](#future-plans)

## Installation
Follow these steps to set up the project locally:
### 1. Clone the Repository
``` bash
git clone https://github.com/codingwitharmand/toolbox-api.git
cd toolbox-api
```
### 2. Create a Virtual Environment
It’s recommended to use a virtual environment to manage dependencies.
``` bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```
### 3. Install Dependencies
Install the required Python packages using `pip`:
``` bash
pip install -r requirements.txt
```
### 4. Install `yt-dlp`
The project relies on `yt-dlp` for downloading YouTube videos. Make sure it is installed.
#### Install via pip:
``` bash
pip install -U yt-dlp
```
#### Or, install locally:
``` bash
sudo curl -L https://yt-dlp.org/downloads/latest/yt-dlp -o /usr/local/bin/yt-dlp
sudo chmod a+rx /usr/local/bin/yt-dlp
```
Additionally, for merging video/audio in high-quality videos, **ffmpeg** may be required:
``` bash
# macOS/Linux
sudo apt install ffmpeg

# Windows (via Chocolatey)
choco install ffmpeg
```
## Usage
Run the API server using the following command:
``` bash
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```
The application will now be running at [`http://localhost:8000`](). You can test its functionality using tools like `curl`, [Postman](), or a browser's developer tools.
## Project Structure
``` 
toolbox-api/
├── app/
│   ├── __init__.py         # Application initialization
│   ├── main.py             # FastAPI entry point
│   ├── routers/            # API route handlers
│   │   ├── __init__.py     
│   │   ├── mp3.py          # MP3 conversion routes
│   │   ├── youtube.py      # YouTube video downloader routes
│   ├── core/               # Core business logic
│   │   ├── __init__.py
│   │   ├── mp3_converter.py # MP3 conversion logic
│   │   ├── youtube_downloader.py # Video downloader logic
│   │   └── utils.py        # Shared utilities
│   └── config.py           # Project configuration settings
├── docs/                   # Endpoint-specific docs
│   ├── mp3_endpoint.md     # Documentation for MP3 converter
│   ├── youtube_endpoint.md # Documentation for YouTube downloader
├── tests/                  # Unit and integration tests
│   ├── test_mp3_converter.py
│   ├── test_youtube_routes.py
│   ├── test_youtube_downloader.py
├── requirements.txt        # Python dependencies
├── .gitignore              # Ignored files (e.g., virtual environments, __pycache__)
└── README.md               # Project documentation
```
## Testing
The project uses `unittest` for testing core logic and API endpoints.
### Run All Tests
To execute all tests, run:
``` bash
python -m unittest discover tests
```
If you’re using `pytest`, you can run:
``` bash
pytest
```
### Test Scope
1. **MP3 Conversion Tests**:
    - Verify that YouTube videos are successfully converted to MP3 and saved correctly.
    - Handle failure scenarios (invalid URLs, missing files).

2. **YouTube Downloader Tests**:
    - Ensure videos are downloaded in different quality options (low, medium, high, best).
    - Handle scenarios where formats are unsupported or URLs are invalid.

## Technical Details
1. **MP3 Conversion**:
    - Uses `yt-dlp` to extract audio from YouTube videos.
    - Processes audio into MP3 format and outputs to a configurable directory.

2. **YouTube Video Downloader**:
    - Supports different video quality options (`low`, `medium`, `high`, `best`) using `yt-dlp`.
    - Files are saved with appropriate formats (`mp4`, `webm`) under a configurable output directory.
    - Handles merging of audio and video streams using `ffmpeg` when needed.

3. **Extensibility**:
    - The modular structure allows the addition of future utilities to `routers` and `core`.
    - Shared helpers are available in `utils.py`.

Refer to these documents for examples, parameters, and expected responses for each endpoint.
## Future Plans
- Add support for downloading playlists.
- Implement video-to-audio conversions for non-YouTube files.
- Include APIs for web scraping, file format conversion (e.g., CSV to JSON), and more.
- Deploy the API as a production-ready service using Docker or cloud solutions (e.g., AWS, GCP).
