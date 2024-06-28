from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

fastapi_app = FastAPI()


def setup_static_folder(static_folder: str) -> FastAPI:
    fastapi_app.mount("/static", StaticFiles(directory=static_folder), name="static")
    return fastapi_app
