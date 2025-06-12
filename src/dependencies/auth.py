from typing import Annotated
from uuid import UUID

from fastapi import Depends, HTTPException, Request, status
from fastapi.security import OAuth2PasswordBearer

from models.token import TokenData
from utils.auth import TOKEN_COOKIE, TOKEN_ENDPOINT, decode_jwt
from utils.config import ENV

# ruff: noqa: S105
oauth2_scheme = OAuth2PasswordBearer(tokenUrl=TOKEN_ENDPOINT, auto_error=False)


async def get_token(
    request: Request, header_token: Annotated[str, Depends(oauth2_scheme)]
) -> TokenData:
    """access token dependency"""

    token = ""

    if ENV == "dev":  # received on header (dev env, swagger)
        if header_token:
            token = header_token
        elif cookie_token := request.cookies.get(TOKEN_COOKIE):
            token = cookie_token
    elif ENV == "prod":  # received on cookie (prod env)
        if cookie_token := request.cookies.get(TOKEN_COOKIE):
            token = cookie_token

    if not token:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="missing auth token",
        )

    return decode_jwt(token)


async def get_user(
    token: Annotated[TokenData, Depends(get_token)],
) -> UUID:
    """token authenticated user dependency"""
    # TODO validate user exists with db
    return token.sub
