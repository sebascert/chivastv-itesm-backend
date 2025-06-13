# ruff: noqa: B008

from typing import Annotated

from fastapi import APIRouter, Depends

from dependencies.resource import get_comment_by_id, get_video_by_id
from models.response import VideoComment
from utils.types import json

router = APIRouter(
    prefix="/comment",
    tags=["comment"],
)


@router.get("/{video_id}/{start}/{end}")
async def get_comments_in_range(
    video_id: Annotated[str, Depends(get_video_by_id)], start: int, end: int
) -> list[VideoComment]:
    """get video comments in range"""
    raise NotImplementedError()


@router.post("/{video_id}")
async def create_comment(
    video_id: Annotated[str, Depends(get_video_by_id)],
) -> json:
    """create comment in video"""
    raise NotImplementedError()


@router.delete("/{comment_id}")
async def delete_comment(
    comment_id: Annotated[str, Depends(get_comment_by_id)],
) -> json:
    """delete comment entry"""
    raise NotImplementedError()
