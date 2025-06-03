# ruff: noqa: B008

from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Body, Depends
from fastapi.security import OAuth2PasswordRequestForm

from dependencies.auth import get_token, get_user
from models.response import UserProfile
from utils.auth import TokenData
from utils.types import json

router = APIRouter(
    prefix="/user",
    tags=["user"],
)


@router.get("/")
async def get_user_profile(
    user_id: Annotated[UUID, Depends(get_user)], data: UserProfile = Body()
) -> UserProfile:
    """get user profile information"""
    raise NotImplementedError()


@router.delete("/")
async def delete_user(user_id: Annotated[UUID, Depends(get_user)]) -> json:
    """delete user"""
    raise NotImplementedError()


@router.post("/register/")
async def register_user(
    user_id: Annotated[UUID, Depends(get_user)], data: UserProfile = Body()
) -> json:
    """register new user"""
    raise NotImplementedError()


@router.post("/token/")
async def login_user(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> json:
    """user login"""
    raise NotImplementedError()


@router.delete("/token")
async def logout_user(token: Annotated[TokenData, Depends(get_token)]) -> json:
    """user logout"""
    raise NotImplementedError()
