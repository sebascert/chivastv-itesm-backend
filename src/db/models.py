from dataclasses import dataclass
from typing import Any

from sqlalchemy import Result


@dataclass
class DBBaseModel:
    """base database model"""

    def __init__(self, res: Result[Any]) -> None:
        pass

class ComentarioModel(DBBaseModel):
    def __init__(self, data: dict[str, Any]):
        super().__init__(data)
        self.ID = data.get("ID")
        self.usuario_email = data.get("usuario_email")
        self.video_ruta_archivo = data.get("video_ruta_archivo")
        self.fecha = data.get("fecha")
        self.contenido = data.get("contenido")
        self.es_en_vivo = data.get("es_en_vivo")
        self.moderado = data.get("moderado")
