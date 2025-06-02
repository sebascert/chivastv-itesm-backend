# ruff: noqa: B008

from fastapi import APIRouter

from utils.types import json

router = APIRouter(
    prefix="/statistics",
    tags=["statistics"],
)


@router.get("/{video_id}")
async def get_statistics(video_id: str) -> json:
    """get statistics of video"""
    raise NotImplementedError()
