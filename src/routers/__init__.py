import importlib
import pkgutil

from fastapi import FastAPI

import routers


def include_routers(app: FastAPI) -> None:
    for _, name, _ in pkgutil.walk_packages(
        routers.__path__, routers.__name__ + "."
    ):
        module = importlib.import_module(name)
        if not hasattr(module, "router"):
            raise ImportError(f"router module '{name}' has no router attr")
        app.include_router(module.router)
