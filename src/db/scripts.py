from abc import ABC, abstractmethod
from dataclasses import asdict
from pathlib import Path
from typing import Any

from sqlalchemy import Result, text

from db.engine import ENGINE
from db.models import DBBaseModel
from db.script_params import DBBaseScriptParams

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


DDL_SCRIPTS: list[DBBaseScript[None, None]] = []
