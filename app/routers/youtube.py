from pathlib import Path

from fastapi import APIRouter, Query, HTTPException
from fastapi.responses import FileResponse

from app.core.mp3_converter import convert_to_mp3
from app.core.video_downloader import download_video

router = APIRouter(
    prefix="/youtube",
    tags=["YouTube Conversion"]
)

@router.get("/convert-mp3")
async def convert(
    url: str = Query(..., description="The URL of the YouTube video to convert")
):
    try:
        path_to_mp3: Path = convert_to_mp3(url)
        return FileResponse(
            path=path_to_mp3,
            media_type='audio/mpeg',
            filename=path_to_mp3.name
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/download")
async def download_youtube_video(
    url: str = Query(..., description="The URL of the YouTube video to download"),
    quality: str = Query("medium", description="Quality of the video: low, medium, high, best(default: medium)"),
    format: str = Query("mp4", description="Optional format for the video file (default is MP4)")
):
    try:
        video_path = download_video(url, format=format, quality=quality)
        return FileResponse(
            path=video_path,
            media_type='video/mp4' if format == "mp4" else "application/octet-stream",
            filename=video_path.name
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))