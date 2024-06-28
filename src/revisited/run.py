import os

from starlette.staticfiles import StaticFiles

from revisited.core.api import healthy_router
from revisited.core.base import fastapi_app
from revisited.core.routers import fastapi_routers as r
from revisited.endpoints.demo import demo_router

static_file_abspath = os.path.join(os.path.dirname(__file__), "static")


def bootstrap():
    r.add_fastapi_router(fastapi_app, healthy_router)
    r.add_fastapi_router(fastapi_app, demo_router)
    fastapi_app.mount("/static", StaticFiles(directory=static_file_abspath), name="static")


if __name__ == '__main__':
    import uvicorn

    bootstrap()
    uvicorn.run(fastapi_app, host='0.0.0.0', port=8000, log_level='debug')
