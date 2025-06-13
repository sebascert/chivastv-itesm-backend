from db.scripts import DDL_SCRIPTS


def db_setup() -> None:
    """database initialization setupt"""
    for ddl in DDL_SCRIPTS:
        ddl.execute(None)
