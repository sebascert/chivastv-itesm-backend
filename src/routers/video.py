# ruff: noqa: B008

from typing import Annotated
from uuid import UUID
from fastapi import APIRouter, Body, Depends, HTTPException, status

from dependencies.auth import get_user
from dependencies.resource import get_category_by_name, get_video_by_id
from models.response import VideoResource
from utils.types import json

router = APIRouter(
    prefix="/video",
    tags=["video"],
)

# ✅ Lista global de categorías
CATEGORIAS = [
    "Chivas Femenil", "Chivas Varonil", "Clásico De México", "Detrás Del Rebaño",
    "Día A Día Rojiblanco", "El Podcast De Las Chivas", "El Recuerdo", "Entrevistas",
    "Esports", "Highlights On Field", "Historia Sagrada", "Leyendas", "Nación Chivas",
    "Operación Valorant", "Raíces", "Repeticiones", "Resiliencia", "Resumen",
    "Santuario Rojiblanco", "Sub's"
]

# ✅ Ruta para obtener video individual por ID
@router.get("/id/{video_id}")
async def get_video_by_id_route(video_id: str) -> dict:
    """Busca el video en todas las categorías; si no lo encuentra, devuelve uno mock"""
    for category in CATEGORIAS:
        videos = await get_videos_by_category(category)
        for video in videos:
            if video["id"] == video_id:
                return video  # ✅ Devuelve el video real con su type (gratis o suscriptor)

    # 🧱 Fallback si el ID no pertenece a ninguna categoría conocida
    return {
        "id": video_id,
        "title": f"Video {video_id}",
        "category": "NO ES CLASICO",
        "type": "gratis",
        "date": "2025-06-12",
        "duration": "10:03",
        "image": "",
        "url": "https://www.youtube.com/watch?v=VhJtbEEUkMM",
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
            "url": "https://www.youtube.com/watch?v=VhJtbEEUkMM",
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
            "url": "https://www.youtube.com/watch?v=pVv9EDYt-is",
            "description": f"Segundo video de la categoría {category}",
            "partido": True
        }
    ]


# 🚧 Rutas no implementadas aún
from fastapi import HTTPException, status
from typing import Annotated
from uuid import UUID

@router.post("")
async def create_video(
    user: Annotated[dict, Depends(get_user)],
    video_data: dict = Body(...)
):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="No autorizado")
    
    return {
        "message": "Video creado correctamente",
        "video": video_data
    }

@router.delete("/{video_id}")
async def delete_video(
    video_id: str,
    user: Annotated[dict, Depends(get_user)],
) -> dict:
    if user["role"] != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No autorizado")
    
    return {
        "message": f"Video {video_id} eliminado por admin {user['email']}"
    }
