from fastapi import FastAPI

from apis.base import api_router
from core.config import settings
from db.session import create_tables
from db.utils import check_db_connected


def include_router(app):
    app.include_router(api_router)


def start_app():
    """Function to Run app"""
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    include_router(app)
    create_tables()
    return app


app = start_app()


@app.on_event("startup")
async def app_startup():
    await check_db_connected()
