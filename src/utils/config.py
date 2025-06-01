import os
from pathlib import Path

from dotenv import load_dotenv

SRC_DIR = Path(__file__).resolve().parent.parent
load_dotenv(dotenv_path=SRC_DIR / ".env")


def getenv(var: str) -> str:
    """get variable or raise error if it does not exists"""
    res = os.getenv(var)
    if res is None:
        raise OSError(f"missing '{var}' env variable")
    return res


DB_USER = getenv("CHIVASTV_DATABASE_USER")
DB_PSWD = getenv("CHIVASTV_DATABASE_PSWD")
DB_NAME = getenv("CHIVASTV_DATABASE_NAME")
DB_HOST = getenv("CHIVASTV_DATABASE_HOST")
