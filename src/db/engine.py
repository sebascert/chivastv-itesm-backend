from sqlalchemy import create_engine

from utils.config import DB_HOST, DB_NAME, DB_PSWD, DB_USER

ENGINE = create_engine(
    f"mysql+mysqlconnector://{DB_USER}:{DB_PSWD}@{DB_HOST}/{DB_NAME}"
)
