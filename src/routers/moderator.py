# ruff: noqa: B008

from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends

from dependencies.auth import get_user
from dependencies.resource import get_comment_by_id
from utils.types import json

router = APIRouter(
    prefix="/mod",
    tags=["moderation"],
)


@router.delete("/comment")
async def mod_delet_comment(
    user_id: Annotated[UUID, Depends(get_user)],
    comment_id: Annotated[str, Depends(get_comment_by_id)],
) -> json:
    """delete comment as moderator"""
    raise NotImplementedError()
