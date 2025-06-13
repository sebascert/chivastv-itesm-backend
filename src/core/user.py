import uuid
from datetime import datetime
from uuid import UUID

from models.response import UserProfile


def auth_user(username: str, pswd: str) -> UUID | None:
    """authenticate user and get its id"""
    return uuid.uuid4()


def user_role(user: UUID) -> str:
    """get user role by user id"""
    return "free"


def user_profile(id: UUID) -> UserProfile:
    """get user profile by user id"""
    return UserProfile(
        id=id,
        email="jane.doe@example.com",
        name="Jane",
        lastname="Doe",
        genre="female",
        birth_date=datetime(1990, 5, 21),
        occupation="Civil Engineer",
        creation_date=datetime(2025, 6, 12, 10, 30, 0),
        address="742 Evergreen Terrace",
        postal_code="62704",
        state="Illinois",
        city="Springfield",
    )
