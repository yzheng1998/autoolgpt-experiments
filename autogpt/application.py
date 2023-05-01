import os
from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from fastapi.staticfiles import StaticFiles
from autogpt.v1.router import api_router as api_router_v1

from autogpt.lifetime import register_shutdown_event, register_startup_event

APP_ROOT = Path(__file__).parent

def get_app() -> FastAPI:
    """
    Get FastAPI application.

    This is the main constructor of an application.

    :return: application.
    """

    app = FastAPI(
        title="autogpt",
        version=1,
        docs_url=None,
        redoc_url=None,
        openapi_url="/api/openapi.json",
        default_response_class=ORJSONResponse
    )
    # api_router.add_websocket_route("/ws", websocket_endpoint, name="websocket")
    # Adds startup and shutdown events.
    register_startup_event(app)
    register_shutdown_event(app)

    # Main router for the API.
    app.include_router(router=api_router_v1, prefix="/api/v1")

    # Adds static directory.
    # This directory is used to access swagger files.
    app.mount(
        "/static",
        StaticFiles(directory=APP_ROOT / "static"),
        name="static",
    )
    return app
