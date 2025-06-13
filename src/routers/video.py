# ruff: noqa: B008

from typing import Annotated
from uuid import UUID
from fastapi import APIRouter, Body, Depends

from dependencies.auth import get_user
from dependencies.resource import get_category_by_name, get_video_by_id
from models.response import VideoResource
from utils.types import json

router = APIRouter(
    prefix="/video",
    tags=["video"],
)

# ✅ Ruta original
@router.get("/id/{video_id}")
async def get_video_by_id_route(video_id: str) -> dict:
    """Devuelve un solo video (vía /video/id/{video_id})"""
    return {
        "id": video_id,
        "title": f"Video {video_id}",
        "category": "NO ES CLASICO",
        "type": "gratis",
        "date": "2025-06-12",
        "duration": "10:03",
        "image": "",
        "url": "https://www.youtube.com/watch?v=3OdyM-Yvd3k",
        "description": f"Este es un video individual con ID {video_id}",
        "partido": True
    }

# ✅ Ruta alternativa que acepta /video/{video_id}
@router.get("/{video_id}")
async def get_video_fallback(video_id: str) -> dict:
    """Ruta alternativa para compatibilidad (/video/{video_id})"""
    return await get_video_by_id_route(video_id)

# ✅ Ruta para videos por categoría
@router.get("/categoria/{category}")
async def get_videos_by_category(category: str) -> list[dict]:
    return [
        {
            "id": f"{category}-1",
            "title": f"{category} Video 1",
            "category": category,
            "type": "gratis",
            "date": "2025-06-12",
            "duration": "10:03",
            "image": "",
            "url": "https://www.youtube.com/watch?v=EAZ48zMjmKo",
            "description": f"Primer video de la categoría {category}",
            "partido": False
        },
        {
            "id": f"{category}-2",
            "title": f"{category} Video 2",
            "category": category,
            "type": "suscriptor",
            "date": "2025-06-13",
            "duration": "12:45",
            "image": "",
            "url": "https://www.youtube.com/watch?v=EAZ48zMjmKo",
            "description": f"Segundo video de la categoría {category}",
            "partido": True
        }
    ]


# 🚧 Rutas no implementadas aún
@router.post("/{video_id}")
async def create_video(
    video_id: Annotated[str, Depends(get_video_by_id)],
    user_id: Annotated[UUID, Depends(get_user)],
) -> json:
    raise NotImplementedError()

@router.delete("/{video_id}")
async def delete_video(
    video_id: Annotated[str, Depends(get_video_by_id)],
    user_id: Annotated[UUID, Depends(get_user)],
) -> json:
    raise NotImplementedError()

@router.put("/{video_id}")
async def update_video(
    video_id: Annotated[str, Depends(get_video_by_id)],
    user_id: Annotated[UUID, Depends(get_user)],
    data: VideoResource = Body(),
) -> json:
    raise NotImplementedError()
