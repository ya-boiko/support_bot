"""Main script."""

from fastapi import FastAPI

from app import rest_api
from app.container import Container
from app.settings import Settings


def create_app():
    """Creates the application."""
    container = Container()
    container.config.from_dict(Settings().model_dump())

    return build_app()


def build_app():
    """Builds the application."""
    app = FastAPI(
        title='Support bot',
        docs_url='/api/docs',
        openapi_url='/api/openapi.json',
    )

    app.include_router(rest_api.support_router)

    return app
