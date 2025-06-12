from dataclasses import dataclass
from typing import Any

from sqlalchemy import Result


@dataclass
class DBBaseModel:
    """base database model"""

    def __init__(self, res: Result[Any]) -> None:
        pass
