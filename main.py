from fastapi import FastAPI

from apis.base import api_router
from core.config import settings
from db.session import create_tables
import asyncio


def include_router(app):
    app.include_router(api_router)


def start_app():
    """Function to Run app"""
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    include_router(app)
    asyncio.create_task(create_tables())
    return app


app = start_app()
