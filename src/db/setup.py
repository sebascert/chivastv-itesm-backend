
from db.scripts import (
    DDL_SCRIPTS,
    DBCreateProcedures,
    DBCreateTriggers,
    DBCreateViews
)

def db_setup():
    print("▶ Creando tablas...")
    for ddl in DDL_SCRIPTS:
        print(f"⏳ Ejecutando {ddl.__name__}")
        ddl.execute(None)

    print("▶ Ejecutando procedimientos...")
    DBCreateProcedures.execute(None)

    print("▶ Ejecutando vistas...")
    DBCreateViews.execute(None)

    print("▶ Ejecutando triggers...")
    DBCreateTriggers.execute(None)

    print("✅ Base de datos lista.")
