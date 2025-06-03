import datetime as dt
from datetime import datetime

import jwt
from fastapi import HTTPException, status
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext

from models.token import TokenData
from utils.config import JWT_ALGORITHM, JWT_SECRET_KEY

# Password hashing setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

CREDENTIALS_EXCEPTION = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


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
