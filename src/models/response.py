from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class UserProfile(BaseModel):
    id: UUID
    email: str
    name: str
    lastname: str

    genre: str
    birth_date: datetime
    occupation: str

    creation_date: datetime

    address: str
    postal_code: str
    state: str
    city: str


# VIDEO


class VideoCategory(BaseModel):
    name: str


class VideoResource(BaseModel):
    id: UUID
    owner: UUID

    title: str
    description: str
    category: VideoCategory
    creation_date: datetime

    url: str


class VideoComment(BaseModel):
    owner: UUID
    video: UUID
    content: str
    creation_date: datetime


# STATISTICS


class Sanction(BaseModel):
    type: str
    description: str


class TeamStatistics(BaseModel):
    name: str
    goals: int
    sanctions: list[Sanction]


class VideoStatistics(BaseModel):
    video: UUID

    team_a: TeamStatistics
    team_b: TeamStatistics
