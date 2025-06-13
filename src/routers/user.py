# ruff: noqa: B008

from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Body, Depends, HTTPException, Response, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm

from core.user import auth_user, user_profile, user_role
from dependencies.auth import get_token, get_user
from models.response import UserProfile
from utils.auth import TOKEN_COOKIE, TokenData, encode_jwt, set_token_cookie
from utils.config import ENV
from utils.types import json

router = APIRouter(
    prefix="/user",
    tags=["user"],
)


@router.get("/")
async def get_user_profile(
    user_id: Annotated[UUID, Depends(get_user)],
) -> UserProfile:
    """get user profile information"""
    return user_profile(user_id)


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
) -> Response:
    """user login"""

    user = auth_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña invalidos",
        )

    role = user_role(user)
    token = encode_jwt(TokenData.create(user, role))

    response: JSONResponse
    if ENV == "dev":  # return token in response
        response = JSONResponse(
            content={
                TOKEN_COOKIE: token,
                "token_type": "bearer",
            }
        )
    elif ENV == "prod":  # return token on secure HttpOnly cookie
        response = JSONResponse(
            content={"message": "token supplied on HttpOnly cookie"}
        )
        set_token_cookie(response, token)
    return response


@router.delete("/token/")
async def logout_user(
    token: Annotated[TokenData, Depends(get_token)],
) -> Response:
    """user logout"""
    response = JSONResponse(
        content={"message": "token successfully forgotten"}
    )
    set_token_cookie(response, "")
    return response
