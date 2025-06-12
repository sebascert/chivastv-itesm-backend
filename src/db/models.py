from abc import ABC
from typing import Any

from sqlalchemy import Result


class BDBaseModel(ABC):
    """base database model"""

    def __init__(self, res: Result[Any]) -> None:
        pass
