import datetime as dt
import re
from datetime import datetime, timedelta

import jwt
from fastapi import HTTPException, Response, status
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext

from models.token import TokenData
from utils.config import JWT_ALGORITHM, JWT_EXPIRE_MINUTES, JWT_SECRET_KEY

# Password hashing setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

CREDENTIALS_EXCEPTION = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)

# ruff: noqa: S105
TOKEN_COOKIE = "access_token"
TOKEN_ENDPOINT = "user/token"

# at least length 4, and only alnum chars
USERNAME_REGEX = r"^[a-zA-Z0-9]{4,}$"
# at least length 10, and only alnum and [!@#$%^&*(),.?\":{}|<>] chars
PASSWORD_REGEX = r"^[a-zA-Z0-9!@#$%^&*(),.?\":{}|<>]{10,}$"


def valid_username(username: str) -> bool:
    """determines if username if valid"""
    return re.match(USERNAME_REGEX, username) is not None


def valid_pswd(pswd: str) -> bool:
    """determines if password if valid"""
    return re.match(PASSWORD_REGEX, pswd) is not None


def hast_pswd(pswd: str) -> str:
    """hash a plaintext password"""
    return pwd_context.hash(pswd)


def verify_pswd(plain_pswd: str, hashed_pswd: str) -> bool:
    """verify a plaintext pswd against a hash"""
    return pwd_context.verify(plain_pswd, hashed_pswd)


def encode_jwt(data: TokenData) -> str:
    """encode JWT access token"""
    payload = {
        "sub": str(data.sub),
        "role": data.role,
        "exp": int(data.exp.timestamp()),
    }

    return jwt.encode(payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)


def decode_jwt(token: str) -> TokenData:
    """decode and validate JWT access token"""
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        payload["exp"] = datetime.fromtimestamp(payload["exp"], tz=dt.UTC)
        return TokenData(**payload)
    except (InvalidTokenError, ValueError) as e:
        raise ValueError("Invalid token") from e


def set_token_cookie(response: Response, token: str) -> None:
    response.set_cookie(
        key=TOKEN_COOKIE,
        value=token,
        httponly=True,
        secure=True,  # enables https security, TODO configure in env var
        samesite="lax",
        max_age=int(timedelta(minutes=JWT_EXPIRE_MINUTES).total_seconds()),
        path="/user/token",
    )
