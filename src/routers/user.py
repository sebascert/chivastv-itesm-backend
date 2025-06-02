# ruff: noqa: B008

from fastapi import APIRouter

from utils.types import json

router = APIRouter(
    prefix="/user",
    tags=["user"],
)


@router.get("/")
async def get_user() -> json:
    """get user profile information"""
    raise NotImplementedError()


@router.delete("/")
async def delete_user() -> json:
    """delete user"""
    raise NotImplementedError()


@router.post("/register/{user_id}")
async def register_user(user_id: str) -> json:
    """register new user"""
    raise NotImplementedError()


@router.post("/login/{user_id}")
async def login_user(user_id: str) -> json:
    """user login"""
    raise NotImplementedError()


@router.post("/logout")
async def logout_user() -> json:
    """user logout"""
    raise NotImplementedError()
