import datetime as dt
from datetime import datetime, timedelta
from uuid import UUID

from pydantic import BaseModel

from utils.config import JWT_EXPIRE_MINUTES


class TokenData(BaseModel):
    exp: datetime
    sub: UUID
    role: str

    @classmethod
    def create(
        cls, sub: UUID, role: str, expires_delta: timedelta | None = None
    ) -> "TokenData":
        """create TokenData instance with default expiration"""
        exp = datetime.now(dt.UTC) + (
            expires_delta or timedelta(minutes=JWT_EXPIRE_MINUTES)
        )
        return cls(sub=sub, role=role, exp=exp)
