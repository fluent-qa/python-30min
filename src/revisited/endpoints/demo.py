from fastapi import APIRouter
from starlette.responses import FileResponse

demo_router = APIRouter(tags=["demos"])


@demo_router.get("/demo/json", status_code=200)
def demo():
    return {"message": "Hello World"}


@demo_router.get("/")
def index():
    return index_html()


@demo_router.get("/demo/static")
def index_html():
    return FileResponse(f"static/index.html")
