from abc import ABC, abstractmethod
from dataclasses import asdict
from pathlib import Path
from typing import Any

from sqlalchemy import Result, text

from db.engine import ENGINE
from db.models import DBBaseModel, ComentarioModel


from db.script_params import (
    DBBaseScriptParams,
    ObtenerComentariosParams,
    InsertarComentarioParams,
    EliminarComentarioParams,
    ObtenerEstadisticasParams,
    RegistrarUsuarioParams,
    LoginUsuarioParams,
    CrearVideoParams,
    ObtenerVideoParams,

)

SCRIPTS_DIR = Path(__file__).resolve().parent / "scripts"


class DBBaseScript[T: DBBaseModel | None, U: DBBaseScriptParams | None](ABC):
    _script: str | None = None

    @classmethod
    def script(cls) -> str:
        if cls._script is None:
            with open(SCRIPTS_DIR / cls.path()) as script:
                cls._script = script.read()
        return cls._script

    @classmethod
    def _execute(cls, params: dict[str, str]) -> Result[Any]:
        """stablish connection and executes script"""
        with ENGINE.begin() as connection:
            return connection.execute(text(cls.script()), params)

    @classmethod
    @abstractmethod
    def path(cls) -> str:
        """path to script"""

    @classmethod
    @abstractmethod
    def model_constructor(cls, result: Result[Any]) -> T:
        """constructor for the model"""

    @classmethod
    def execute(cls, params: U) -> T:
        """execute script and return corresponding db model"""
        result = cls._execute(dict() if params is None else asdict(params))
        return cls.model_constructor(result)


# Data Definition Lang Scripts

class ObtenerComentariosEnRango(DBBaseScript[list[ComentarioModel], ObtenerComentariosParams]):
    @classmethod
    def path(cls) -> str:
        return "dml/simulacion_endpoints.sql"

    @classmethod
    def model_constructor(cls, result: Result[Any]) -> list[ComentarioModel]:
        return [ComentarioModel(dict(row._mapping)) for row in result]


class InsertarComentario(DBBaseScript[None, InsertarComentarioParams]):
    @classmethod
    def path(cls) -> str:
        return "dml/simulacion_endpoints.sql"

    @classmethod
    def model_constructor(cls, result: Result[Any]) -> None:
        return None


class EliminarComentario(DBBaseScript[None, EliminarComentarioParams]):
    @classmethod
    def path(cls) -> str:
        return "dml/simulacion_endpoints.sql"

    @classmethod
    def model_constructor(cls, result: Result[Any]) -> None:
        return None


class ObtenerEstadisticas(DBBaseScript[list[dict], ObtenerEstadisticasParams]):
    @classmethod
    def path(cls) -> str:
        return "dml/simulacion_endpoints.sql"

    @classmethod
    def model_constructor(cls, result: Result[Any]) -> list[dict]:
        return [dict(row._mapping) for row in result]


class RegistrarUsuario(DBBaseScript[None, RegistrarUsuarioParams]):
    @classmethod
    def path(cls) -> str:
        return "dml/simulacion_endpoints.sql"

    @classmethod
    def model_constructor(cls, result: Result[Any]) -> None:
        return None


class LoginUsuario(DBBaseScript[list[dict], LoginUsuarioParams]):
    @classmethod
    def path(cls) -> str:
        return "dml/simulacion_endpoints.sql"

    @classmethod
    def model_constructor(cls, result: Result[Any]) -> list[dict]:
        return [dict(row._mapping) for row in result]


class CrearVideo(DBBaseScript[None, CrearVideoParams]):
    @classmethod
    def path(cls) -> str:
        return "dml/simulacion_endpoints.sql"

    @classmethod
    def model_constructor(cls, result: Result[Any]) -> None:
        return None


class ObtenerVideo(DBBaseScript[list[dict], ObtenerVideoParams]):
    @classmethod
    def path(cls) -> str:
        return "dml/simulacion_endpoints.sql"

    @classmethod
    def model_constructor(cls, result: Result[Any]) -> list[dict]:
        return [dict(row._mapping) for row in result]


class DBCreateCategoriaTable(DBBaseScript[None, None]):
    @classmethod
    def path(cls) -> str:
        return "ddl/categoria.sql"

    @classmethod
    def model_constructor(cls, result: Result[Any]) -> None:
        return None


class DBCreateComentarioTable(DBBaseScript[None, None]):
    @classmethod
    def path(cls) -> str:
        return "ddl/comentario.sql"

    @classmethod
    def model_constructor(cls, result: Result[Any]) -> None:
        return None


class DBCreateEquipoTable(DBBaseScript[None, None]):
    @classmethod
    def path(cls) -> str:
        return "ddl/equipo.sql"

    @classmethod
    def model_constructor(cls, result: Result[Any]) -> None:
        return None


class DBCreatePermisoTable(DBBaseScript[None, None]):
    @classmethod
    def path(cls) -> str:
        return "ddl/permiso.sql"

    @classmethod
    def model_constructor(cls, result: Result[Any]) -> None:
        return None

class DBCreateUsuarioTable(DBBaseScript[None, None]):
    @classmethod
    def path(cls) -> str:
        return "ddl/usuario.sql"

    @classmethod
    def model_constructor(cls, result: Result[Any]) -> None:
        return None


class DBCreatePermisoUsuarioTable(DBBaseScript[None, None]):
    @classmethod
    def path(cls) -> str:
        return "ddl/permiso_usuario.sql"

    @classmethod
    def model_constructor(cls, result: Result[Any]) -> None:
        return None


class DBCreatePagoPremiumTable(DBBaseScript[None, None]):
    @classmethod
    def path(cls) -> str:
        return "ddl/pago_premium.sql"

    @classmethod
    def model_constructor(cls, result: Result[Any]) -> None:
        return None


class DBCreateSesionTable(DBBaseScript[None, None]):
    @classmethod
    def path(cls) -> str:
        return "ddl/sesion.sql"

    @classmethod
    def model_constructor(cls, result: Result[Any]) -> None:
        return None


class DBCreateEstadisticasPartidoTable(DBBaseScript[None, None]):
    @classmethod
    def path(cls) -> str:
        return "ddl/estadisticas_partido.sql"

    @classmethod
    def model_constructor(cls, result: Result[Any]) -> None:
        return None


class DBCreateFaltaTable(DBBaseScript[None, None]):
    @classmethod
    def path(cls) -> str:
        return "ddl/falta.sql"

    @classmethod
    def model_constructor(cls, result: Result[Any]) -> None:
        return None


class DBCreateModeracionLogTable(DBBaseScript[None, None]):
    @classmethod
    def path(cls) -> str:
        return "ddl/moderacion_log.sql"

    @classmethod
    def model_constructor(cls, result: Result[Any]) -> None:
        return None


class DBCreateVideoTable(DBBaseScript[None, None]):
    @classmethod
    def path(cls) -> str:
        return "ddl/video.sql"

    @classmethod
    def model_constructor(cls, result: Result[Any]) -> None:
        return None

class ObtenerComentariosEnRango(DBBaseScript[None, None]):
    @classmethod
    def path(cls) -> str:
        return "ddl/procedures/obtener_comentarios_en_rango.sql"

    @classmethod
    def model_constructor(cls, result: Result[Any]) -> None:
        return None


class InsertarComentario(DBBaseScript[None, None]):
    @classmethod
    def path(cls) -> str:
        return "ddl/procedures/insertar_comentario.sql"

    @classmethod
    def model_constructor(cls, result: Result[Any]) -> None:
        return None


class EliminarComentario(DBBaseScript[None, None]):
    @classmethod
    def path(cls) -> str:
        return "ddl/procedures/eliminar_comentario.sql"

    @classmethod
    def model_constructor(cls, result: Result[Any]) -> None:
        return None


class ObtenerEstadisticas(DBBaseScript[None, None]):
    @classmethod
    def path(cls) -> str:
        return "ddl/procedures/obtener_estadisticas.sql"

    @classmethod
    def model_constructor(cls, result: Result[Any]) -> None:
        return None


class RegistrarUsuario(DBBaseScript[None, None]):
    @classmethod
    def path(cls) -> str:
        return "ddl/procedures/registrar_usuario.sql"

    @classmethod
    def model_constructor(cls, result: Result[Any]) -> None:
        return None


class LoginUsuario(DBBaseScript[None, None]):
    @classmethod
    def path(cls) -> str:
        return "ddl/procedures/login_usuario.sql"

    @classmethod
    def model_constructor(cls, result: Result[Any]) -> None:
        return None


class CrearVideo(DBBaseScript[None, None]):
    @classmethod
    def path(cls) -> str:
        return "ddl/procedures/crear_video.sql"

    @classmethod
    def model_constructor(cls, result: Result[Any]) -> None:
        return None


class ObtenerVideo(DBBaseScript[None, None]):
    @classmethod
    def path(cls) -> str:
        return "ddl/procedures/obtener_video.sql"

    @classmethod
    def model_constructor(cls, result: Result[Any]) -> None:
        return None

class DBCreateViews(DBBaseScript[None, None]):
    @classmethod
    def path(cls) -> str:
        return "views/views.sql"

    @classmethod
    def model_constructor(cls, result: Result[Any]) -> None:
        return None


class DBCreateTriggers(DBBaseScript[None, None]):
    @classmethod
    def path(cls) -> str:
        return "triggers/all_triggers.sql"  # o usa uno por uno si están separados

    @classmethod
    def model_constructor(cls, result: Result[Any]) -> None:
        return None


DDL_SCRIPTS: list[DBBaseScript[None, None]] = [
    DBCreateUsuarioTable,
    DBCreateCategoriaTable,
    DBCreateEquipoTable,
    DBCreatePermisoTable,
    DBCreateVideoTable,
    DBCreateComentarioTable,
    DBCreatePermisoUsuarioTable,
    DBCreatePagoPremiumTable,
    DBCreateSesionTable,
    DBCreateEstadisticasPartidoTable,
    DBCreateFaltaTable,
    DBCreateModeracionLogTable,
    ObtenerComentariosEnRango,
    InsertarComentario,
    EliminarComentario,
    ObtenerEstadisticas,
    RegistrarUsuario,
    LoginUsuario,
    CrearVideo,
    ObtenerVideo
]



