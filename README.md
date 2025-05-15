# ChivasTV-itesm Backend

API del backend para la pagina ChivasTV-ITESM.

## Dependencias

Se necesita un runtime de python, la version a usar esta en
[pyproject.toml](pyproject.toml), las dependencias se gestionan por medio de
[uv](https://docs.astral.sh/uv), un gestionador de paquetes y proyectos de
python, [guia para instalar
uv](https://docs.astral.sh/uv/getting-started/installation/).

> [Guia para instalar python con
> uv](https://docs.astral.sh/uv/guides/install-python/)

Para agregar dependencias ejecuta:

```bash
# dependencias de la app
uv add <dependency>

# dependencias del entorno de desarrollo
uv add --group dev <dependency>
```

Para instalar las dependencias ejecuta:

```bash
# instala todas las dependencias (tambien de desarrollo)
uv sync

# instala unicamente las dependencias de la app
uv sync --no-dev
```

## Ejecucion

Para ejecutar la api se pueden ejecutar estos comandos por medio de `uv run`, o
activando el [entorno virtual](#entorno-virtual-de-python):

```bash
py src/main.py

# otra manera es utilizando uvicorn directamente
cd src
uvicorn main:app --reload
```

## Analizador estatico y Formatting

El proyecto usa ruff como linter (analizador de codigo estatico) y formatter,
para filtrar errores comunes y mantener un alto estandar de codigo. Este es
instalado por medio de uv, se instala conjunto a las dependencias de
desarrollo.

Se puede utilizar ruff por medio de `uvx ruff`, o despues de activar el
[entorno virtual](#entorno-virtual-de-python) con solo `ruff`.

Para formatear usar:

```bash
ruff check <target-file-or-dir>
```

Para analizar el codigo:

```bash
ruff format <target-file-or-dir>
```

Para organizar los imports:

```bash
ruff check --fix --select I
```

## Entorno Virtual de Python

El entorno virtual de python se puede usar en una de las siguentes maneras:

1. Ejecuta un comando dentro del entorno virtual:

```bash
uv run <cmd>
```

2. Activa el entorno en la sesion de terminal actual, (despues de `uv sync`):

```bash
source .venv/bin/activate
```

Para desactivar el entorno virtual ejecuta:

```bash
deactivate
```
