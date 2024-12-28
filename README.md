# Toolbox API

**Toolbox API** is a FastAPI-based application that provides a collection of utilities and tools. The current version includes a feature to convert YouTube videos to MP3 format and return the converted file as a downloadable response.

---

## Features

- Convert YouTube videos to MP3 format via HTTP API
- Easy to extend with additional tools and utilities
- Organized and scalable project structure
- Runs on `http://localhost:8000` by default

---

## Installation

### 1. Clone the Repository
```shell script
git clone https://github.com/your-username/toolbox-api.git
cd toolbox-api
```

### 2. Create a Virtual Environment
It’s recommended to use a virtual environment to manage dependencies.

```shell script
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### 3. Install Dependencies
Install the required Python packages using `pip`:

```shell script
pip install -r requirements.txt
```

### 4. Install `yt-dlp`
This project relies on the `yt-dlp` tool to download and extract audio from YouTube videos. Make sure `yt-dlp` is installed:

#### Install via pip:
```shell script
pip install -U yt-dlp
```

#### Or, install locally:
```shell script
sudo curl -L https://yt-dlp.org/downloads/latest/yt-dlp -o /usr/local/bin/yt-dlp
sudo chmod a+rx /usr/local/bin/yt-dlp
```

---

## Usage

### 1. Run the Application
You can start the FastAPI application using `uvicorn`:

```shell script
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

The application will now be running on `http://localhost:8000`.

---

### 2. Convert a YouTube Video to MP3

Use the endpoint `/mp3/convert` to convert a YouTube video to MP3 format. Provide the YouTube video URL as a query parameter.

#### Example Request
Make a GET request to:
```
http://127.0.0.1:8000/mp3/convert?url=https://www.youtube.com/watch?v=VIDEO_ID
```

#### Example cURL Command
```shell script
curl -X GET "http://127.0.0.1:8000/mp3/convert?url=https://www.youtube.com/watch?v=VIDEO_ID" --output output.mp3
```

**Response**:
- If successful, the server will return the MP3 file as a downloadable response.
- If there’s an error, the server will return a 500 status code with an error message.

---

## Project Structure

```
project_root/
├── app/                    # Application code
│   ├── __init__.py         # Package initialization
│   ├── main.py             # FastAPI app entry point
│   ├── routers/            # API route handlers
│   │   ├── __init__.py
│   │   ├── mp3.py          # MP3 conversion routes
│   ├── core/               # Core business logic
│   │   ├── __init__.py
│   │   ├── mp3_converter.py   # MP3 conversion logic
│   │   ├── utils.py        # Shared utilities
│   └── config.py           # Configuration settings
├── tests/                  # Unit and integration tests
│   ├── test_mp3_converter.py
│   ├── test_routes.py
│   └── other_tests.py
├── requirements.txt        # Python dependencies
├── .gitignore              # Ignored files (e.g., venv, __pycache__)
└── README.md               # Documentation of the project
```

---

## Environment and Configuration

The application defaults to storing MP3 files in a temporary folder (`output/mp3`) created in the project root at runtime. You can modify this behavior in the `app/config.py` file.

---

## Testing

Unit tests are provided to ensure functionality of key components.

### Run All Tests
Using the `unittest` framework:
```shell script
python -m unittest discover tests
```

Using `pytest` (if you prefer):
```shell script
pytest
```

---

## Future Features

The Toolbox API is designed to be extensible. Planned features include:
- Image processing (e.g., resizing, format conversion)
- File format converters (e.g., CSV to JSON)
- Text extraction from PDFs and images
- Video-to-audio conversion for formats beyond YouTube
- Additional tools as needed by users

---

## Contributing

Contributions are welcome! If you’d like to add features, improve documentation, or fix bugs:
1. Fork the repository.
2. Create a new branch for your feature/bugfix.
3. Submit a pull request.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/) for powering the server
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) for the YouTube download and audio extraction
- Special thanks to contributors and the open-source community.

---

Let me know if you’d like to adjust this further!
