from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from utils.config import DB_HOST, DB_NAME, DB_PSWD, DB_USER

ENGINE = create_engine(
    f"mysql+mysqlconnector://{DB_USER}:{DB_PSWD}@{DB_HOST}/{DB_NAME}"
)

SessionLocal = sessionmaker(bind=ENGINE)

@contextmanager
def db_session():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
