from abc import ABC, abstractmethod
from collections.abc import Callable
from pathlib import Path
from typing import Any

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
    def _execute(cls, **params: str) -> Result[Any]:
        """stablish connection and executes script"""
        with db_session() as session:
            res = session.execute(text(cls.script()), params)
            return res

    @classmethod
    @abstractmethod
    def path(cls) -> str:
        """path to script"""

    @classmethod
    def execute(cls, **params: str) -> T:
        """execute script and return corresponding db model"""
        return cls.model_cons(cls._execute(**params))


# Data Definition Lang Scripts


class DBCreateUserTable(DBBaseScript[EmptyDBModel]):
    model_cons = EmptyDBModel

    @classmethod
    def path(cls) -> str:
        return "ddl/user.sql"


DDL_SCRIPTS = [DBCreateUserTable]
