# ruff: noqa: B008
from fastapi.responses import JSONResponse
from fastapi import Depends, HTTPException, status, Request
from .user import get_user



from typing import Annotated

from fastapi import APIRouter, Depends

from dependencies.resource import get_comment_by_id, get_video_by_id
from models.response import VideoComment
from utils.types import json

router = APIRouter(
    prefix="/comment",
    tags=["comment"],
)


@router.get("/{video_id}/{start}/{end}")
async def get_comments_in_range(video_id: str, start: int, end: int) -> list[dict]:
    """Simulación de comentarios por video"""
    return [
        {
            "id": "c1",
            "user": "usuario1",
            "content": "Gran partido",
            "timestamp": "2024-12-05T14:00:00Z"
        },
        {
            "id": "c2",
            "user": "rojiblanco97",
            "content": "Este análisis estuvo brutal",
            "timestamp": "2024-12-05T15:30:00Z"
        }
    ][start:end]


@router.post("/{video_id}")
async def create_comment(video_id: str, request: Request):
    """Simula creación de comentario"""
    body = await request.json()
    content = body.get("content", "")

    # Puedes simular guardar o solo devolver el resultado
    return JSONResponse(content={
        "id": "fake-id",
        "video_id": video_id,
        "user": "mock-user",
        "content": content,
        "timestamp": "2025-06-12T00:00:00Z"
    })  


@router.delete("/{comment_id}")
async def delete_comment(
    comment_id: Annotated[str, Depends(get_comment_by_id)],
    user: Annotated[dict, Depends(get_user)],  # Asegura que get_user devuelva el perfil
) -> dict:
    if user["role"] != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No autorizado para eliminar comentarios")
    
    return {
        "message": f"Comentario {comment_id} eliminado por admin {user['email']}"
    }
