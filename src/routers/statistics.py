# ruff: noqa: B008

from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends

from dependencies.auth import get_user
from dependencies.resource import get_video_by_id
from models.response import VideoStatistics

router = APIRouter(
    prefix="/statistics",
    tags=["statistics"],
)


@router.get("/{video_id}")
async def get_statistics(
    user_id: Annotated[UUID, Depends(get_user)],
    video_id: Annotated[UUID, Depends(get_video_by_id)],
) -> VideoStatistics:
    """get statistics of video"""
    raise NotImplementedError()
