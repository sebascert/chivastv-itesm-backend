from dataclasses import dataclass
from typing import Any

from sqlalchemy import Result


@dataclass
class DBBaseModel:
    """base database model"""

    def __init__(self, res: Result[Any]) -> None:
        pass
from abc import ABC


class DBBaseModel(ABC):
    """Base para todos los modelos construidos desde resultados SQL."""
    def __init__(self, data: dict[str, Any]) -> None:
        self._data = data


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

    def __repr__(self) -> str:
        return f"<Comentario {self.ID} {self.usuario_email}>"


class UsuarioModel(DBBaseModel):
    def __init__(self, data: dict[str, Any]):
        super().__init__(data)
        self.ID = data.get("ID")
        self.email = data.get("email")
        self.nombre = data.get("nombre")
        self.apellido = data.get("apellido")
        self.genero = data.get("genero")
        self.fecha_nacimiento = data.get("fecha_nacimiento")
        self.fecha_creacion = data.get("fecha_creacion")
        self.direccion = data.get("direccion")
        self.ciudad = data.get("ciudad")
        self.estado = data.get("estado")
        self.pais = data.get("pais")

    def __repr__(self) -> str:
        return f"<Usuario {self.ID} {self.email}>"


class VideoModel(DBBaseModel):
    def __init__(self, data: dict[str, Any]):
        super().__init__(data)
        self.ID = data.get("ID")
        self.ruta_archivo = data.get("ruta_archivo")
        self.titulo = data.get("titulo")
        self.descripcion = data.get("descripcion")
        self.fecha_subida = data.get("fecha_subida")
        self.categoria_nombre = data.get("categoria_nombre")
        self.es_publico = data.get("es_publico")
        self.es_premium = data.get("es_premium")
        self.es_partido = data.get("es_partido")
        self.deleted = data.get("deleted")

    def __repr__(self) -> str:
        return f"<Video {self.ID} {self.titulo}>"


class EstadisticaPartidoModel(DBBaseModel):
    def __init__(self, data: dict[str, Any]):
        super().__init__(data)
        self.video_ruta_archivo = data.get("video_ruta_archivo")
        self.equipoA_nombre = data.get("equipoA_nombre")
        self.equipoB_nombre = data.get("equipoB_nombre")
        self.golesA = data.get("golesA")
        self.golesB = data.get("golesB")
        self.falta_descripcion = data.get("falta_descripcion")
        self.momento = data.get("momento")

    def __repr__(self) -> str:
        return f"<Estadisticas {self.video_ruta_archivo}>"


class PermisoUsuarioModel(DBBaseModel):
    def __init__(self, data: dict[str, Any]):
        super().__init__(data)
        self.user_ID = data.get("user_ID")
        self.permiso_nombre = data.get("permiso_nombre")

    def __repr__(self) -> str:
        return f"<PermisoUsuario {self.user_ID} {self.permiso_nombre}>"


class PagoPremiumModel(DBBaseModel):
    def __init__(self, data: dict[str, Any]):
        super().__init__(data)
        self.referencia_pasarela = data.get("referencia_pasarela")
        self.usuario_email = data.get("usuario_email")
        self.fecha_pago = data.get("fecha_pago")
        self.metodo = data.get("metodo")
        self.monto = data.get("monto")
        self.fue_exitoso = data.get("fue_exitoso")

    def __repr__(self) -> str:
        return f"<PagoPremium {self.referencia_pasarela}>"


class ModeracionLogModel(DBBaseModel):
    def __init__(self, data: dict[str, Any]):
        super().__init__(data)
        self.ID = data.get("ID")
        self.email = data.get("email")
        self.video_ruta_archivo = data.get("video_ruta_archivo")
        self.fecha = data.get("fecha")
        self.accion = data.get("accion")

    def __repr__(self) -> str:
        return f"<ModeracionLog {self.ID}>"
