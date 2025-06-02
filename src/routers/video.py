# ruff: noqa: B008

from fastapi import APIRouter

from utils.types import json

router = APIRouter(
    prefix="/video",
    tags=["video"],
)


@router.get("/{video_id}")
async def get_video(video_id: str) -> json:
    """get video information"""
    raise NotImplementedError()


@router.post("{video_id}/")
async def create_video(video_id: str) -> json:
    """create video entry"""
    raise NotImplementedError()


@router.delete("{video_id}/")
async def delete_video(video_id: str) -> json:
    """delete video entry"""
    raise NotImplementedError()


@router.get("/{category}")
async def get_videos_by_category() -> json:
    """get videos by category"""
    raise NotImplementedError()


@router.put("{video_id}/")
async def update_video(video_id: str) -> json:
    """update video information"""
    raise NotImplementedError()
