from fastapi import FastAPI
from backend.core.config import settings



def start_app():
    """ Function to Run app"""
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    
    return app


app = start_app()