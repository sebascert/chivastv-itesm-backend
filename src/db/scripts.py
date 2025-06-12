from abc import ABC, abstractmethod
from collections.abc import Callable
from operator import rshift
from pathlib import Path
from typing import Any
import sqlparse

from sqlalchemy import Result, text

from db.models import BDBaseModel, EmptyDBModel
from db.session import db_session

SCRIPTS_DIR = Path(__file__).resolve().parent / "scripts"

class DBBaseScript[T: BDBaseModel](ABC):
    _script: str | None = None
    model_cons: Callable[[Result[Any]], T]

    @classmethod
    def script(cls) -> str:
        if cls._script is None:
            with open(SCRIPTS_DIR / cls.path()) as script:
                cls._script = script.read()
        return cls._script

    @classmethod
    def _execute(cls, **params: str) -> list[Result[Any]]:
        """establish connection and executes script"""

        results = []
        with db_session() as session:

            stms = [stmt.strip() for stmt in sqlparse.split(cls.script()) if stmt.strip()]

            for stmt in stms:

                process_stmt = text(stmt).execution_options(stream_results=False)
                result = session.execute(process_stmt, params)

                # Consumimos resultado por seguridad (especialmente en triggers y views)
                try:
                    result.fetchall()
                except Exception:
                    pass

                results.append(result)

        return results

    @classmethod
    @abstractmethod
    def path(cls) -> str:
        """path to script"""

    @classmethod
    def execute(cls, **params: str) -> T:
        """execute script and return corresponding db model"""
        return cls.model_cons(cls._execute(**params))


# Data Definition Lang Scripts
class DBCreateSchema(DBBaseScript[EmptyDBModel]):
    model_cons = EmptyDBModel

    @classmethod
    def path(cls) -> str:
        return "DB.sql"

class DBCreateCategoryTable(DBBaseScript[EmptyDBModel]):
    model_cons = EmptyDBModel

    @classmethod
    def path(cls) -> str:
        return "categoria.sql"

class DBCreateTeamTable(DBBaseScript[EmptyDBModel]):
    model_cons = EmptyDBModel

    @classmethod
    def path(cls) -> str:
        return "equipo.sql"

class DBCreatePermitTable(DBBaseScript[EmptyDBModel]):
    model_cons = EmptyDBModel

    @classmethod
    def path(cls) -> str:
        return "permiso.sql"

class DBCreateUserTable(DBBaseScript[EmptyDBModel]):
    model_cons = EmptyDBModel

    @classmethod
    def path(cls) -> str:
        return "usuario.sql"

class DBCreatePremiumPayTable(DBBaseScript[EmptyDBModel]):
    model_cons = EmptyDBModel

    @classmethod
    def path(cls) -> str:
        return "pago_premium.sql"

class DBCreateUserPermitTable(DBBaseScript[EmptyDBModel]):
    model_cons = EmptyDBModel

    @classmethod
    def path(cls) -> str:
        return "permiso_usuario.sql"

class DBCreateSessionTable(DBBaseScript[EmptyDBModel]):
    model_cons = EmptyDBModel

    @classmethod
    def path(cls) -> str:
        return "sesion.sql"

class DBCreateVideoTable(DBBaseScript[EmptyDBModel]):
    model_cons = EmptyDBModel

    @classmethod
    def path(cls) -> str:
        return "video.sql"

class DBCreateCommentTable(DBBaseScript[EmptyDBModel]):
    model_cons = EmptyDBModel

    @classmethod
    def path(cls) -> str:
        return "comentario.sql"

class DBCreateEstadisticasPartidoTable(DBBaseScript[EmptyDBModel]):
    model_cons = EmptyDBModel

    @classmethod
    def path(cls) -> str:
        return "estadisticas_partido.sql"


class DBCreateFaltaTable(DBBaseScript[EmptyDBModel]):
    model_cons = EmptyDBModel

    @classmethod
    def path(cls) -> str:
        return "falta.sql"

class DBCreateModerationLogTable(DBBaseScript[EmptyDBModel]):
    model_cons = EmptyDBModel

    @classmethod
    def path(cls) -> str:
        return "moderacion_log.sql"


class DBInsertDMLScript(DBBaseScript[EmptyDBModel]):
    model_cons = EmptyDBModel

    @classmethod
    def path(cls) -> str:
        return "DML.sql"

class DBTriggerUpdateUsuario(DBBaseScript[EmptyDBModel]):
    model_cons = EmptyDBModel

    @classmethod
    def path(cls) -> str:
        return "trigger_update_usuario.sql"

class DBTriggerVideoDelete(DBBaseScript[EmptyDBModel]):
    model_cons = EmptyDBModel

    @classmethod
    def path(cls) -> str:
        return "trigger_video_delete.sql"

class DBTriggerModLog(DBBaseScript[EmptyDBModel]):
    model_cons = EmptyDBModel

    @classmethod
    def path(cls) -> str:
        return "trigger_mod_log.sql"

class DBViews(DBBaseScript[EmptyDBModel]):
    model_cons = EmptyDBModel

    @classmethod
    def path(cls) -> str:
        return "views.sql"


DDL_SCRIPTS: list[DBBaseScript[Any]] = [
    DBCreateSchema,
    DBCreateCategoryTable,
    DBCreateTeamTable,
    DBCreatePermitTable,
    DBCreateUserTable,
    DBCreatePremiumPayTable,
    DBCreateUserPermitTable,
    DBCreateSessionTable,
    DBCreateVideoTable,
    DBCreateCommentTable,
    DBCreateEstadisticasPartidoTable,
    DBCreateFaltaTable,
    DBCreateModerationLogTable,
    DBTriggerUpdateUsuario,
    DBTriggerVideoDelete,
    DBTriggerModLog,
    DBViews
]




