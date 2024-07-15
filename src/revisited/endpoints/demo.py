from typing import Dict

from fastapi import APIRouter
from starlette.responses import FileResponse

demo_router = APIRouter(tags=["demos"])


@demo_router.get("/demo/json", status_code=200)
def demo() -> dict:
    return {"message": "Hello World"}


@demo_router.get("/")
def index():
    return FileResponse("static/index.html")


@demo_router.get("/demo/{path_name}", status_code=200)
def path_var(path_name: str) -> dict[str, str]:
    return {"message": f"{path_name} from path request"}


@demo_router.get("/demo/static")
def index_html():
    return FileResponse("static/index.html")
