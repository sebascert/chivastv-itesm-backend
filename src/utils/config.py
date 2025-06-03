import os
from collections.abc import Callable
from pathlib import Path

from dotenv import load_dotenv

SRC_DIR = Path(__file__).resolve().parent.parent
load_dotenv(dotenv_path=SRC_DIR / ".env")


def getenv[T](var: str, constructor: Callable[[str], T]) -> T:
    """get and validate environment variable"""
    value = os.getenv(var)
    if value is None:
        raise OSError(f"missing '{var}' env variable")
    try:
        return constructor(value)
    except (TypeError, ValueError) as e:
        raise OSError(
            f"env variable '{var}' of value '{value}' has invalid type"
        ) from e


# DATABASE
DB_USER = getenv("CHIVASTV_DATABASE_USER", str)
DB_PSWD = getenv("CHIVASTV_DATABASE_PSWD", str)
DB_NAME = getenv("CHIVASTV_DATABASE_NAME", str)
DB_HOST = getenv("CHIVASTV_DATABASE_HOST", str)

# JWT
JWT_SECRET_KEY = getenv("CHIVASTV_JWT_SECRET_KEY", str)
JWT_ALGORITHM = getenv("CHIVASTV_JWT_ALGORITHM", str)
JWT_EXPIRE_MINUTES = getenv("CHIVASTV_JWT_EXPIRE_MINUTES", float)
