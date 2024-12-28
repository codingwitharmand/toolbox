from pathlib import Path

from fastapi import APIRouter, Query, HTTPException
from fastapi.responses import FileResponse

from app.core.mp3_converter import convert_to_mp3

router = APIRouter(
    prefix="/mp3",
    tags=["MP3 Conversion"]
)

@router.get("/convert")
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