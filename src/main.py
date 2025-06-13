import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.video import router as video_router


from db.setup import db_setup
from routers import include_routers
from utils.types import json

db_setup()

app = FastAPI()
app.include_router(video_router)

include_routers(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


@app.get("/")
async def root() -> json:
    return {"message": "ChivasTV Backend"}


def main() -> None:
    print("ChivasTV Backend\n")
    uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()
