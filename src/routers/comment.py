# ruff: noqa: B008

from fastapi import APIRouter

from utils.types import json

router = APIRouter(
    prefix="/comment",
    tags=["comment"],
)


@router.get("/{video_id}/{start}/{end}")
async def get_comments_in_range(video_id: str, start: int, end: int) -> json:
    """get video comments in range"""
    raise NotImplementedError()


@router.post("/{video_id}")
async def create_comment(video_id: str) -> json:
    """create comment in video"""
    raise NotImplementedError()


@router.delete("/{comment_id}")
async def delete_commen(comment_id: str) -> json:
    """delete comment entry"""
    raise NotImplementedError()
