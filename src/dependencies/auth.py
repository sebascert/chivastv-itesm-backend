from typing import Annotated
from uuid import UUID

from fastapi import Depends, HTTPException, Request, status
from fastapi.security import OAuth2PasswordBearer

from utils.auth import TokenData, decode_jwt

# ruff: noqa: S105
TOKEN_ENDPOINT = "user/token/"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl=TOKEN_ENDPOINT, auto_error=False)


async def get_token(
    request: Request, header_token: Annotated[str, Depends(oauth2_scheme)]
) -> TokenData:
    """access token dependency"""
    # received on header (swagger)
    if header_token:
        return decode_jwt(header_token)

    # received on cookie (prod env)
    cookie_token = request.cookies.get("access_token")
    if cookie_token:
        return decode_jwt(cookie_token)

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="missing auth token",
    )


async def get_user(
    token: Annotated[TokenData, Depends(get_token)],
) -> UUID:
    """token authenticated user dependency"""
    # TODO validate user exists with db
    return token.sub
