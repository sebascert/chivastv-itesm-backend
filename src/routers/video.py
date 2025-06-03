# ruff: noqa: B008

from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Body, Depends

from dependencies.auth import get_user
from dependencies.resource import get_category_by_name, get_video_by_id
from models.response import VideoResource
from utils.types import json

router = APIRouter(
    prefix="/video",
    tags=["video"],
)


@router.get("/{video_id}")
async def get_video(
    video_id: Annotated[str, Depends(get_video_by_id)],
    user_id: Annotated[UUID, Depends(get_user)],
) -> VideoResource:
    """get video information"""
    raise NotImplementedError()


@router.post("{video_id}/")
async def create_video(
    video_id: Annotated[str, Depends(get_video_by_id)],
    user_id: Annotated[UUID, Depends(get_user)],
) -> json:
    """create video entry"""
    raise NotImplementedError()


@router.delete("{video_id}/")
async def delete_video(
    video_id: Annotated[str, Depends(get_video_by_id)],
    user_id: Annotated[UUID, Depends(get_user)],
) -> json:
    """delete video entry"""
    raise NotImplementedError()


@router.get("/{category}")
async def get_videos_by_category(
    category: Annotated[str, Depends(get_category_by_name)],
    user_id: Annotated[UUID, Depends(get_user)],
) -> list[VideoResource]:
    """get videos by category"""
    raise NotImplementedError()


@router.put("{video_id}/")
async def update_video(
    video_id: Annotated[str, Depends(get_video_by_id)],
    user_id: Annotated[UUID, Depends(get_user)],
    data: VideoResource = Body(),
) -> json:
    """update video information"""
    raise NotImplementedError()
