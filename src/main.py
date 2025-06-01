import uvicorn
from fastapi import FastAPI

from utils.types import json

app = FastAPI()


@app.get("/")
async def root() -> json:
    return {"message": "ChivasTV Backend"}


def main() -> None:
    print("ChivasTV Backend\n")
    uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()
