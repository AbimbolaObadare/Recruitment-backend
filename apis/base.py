from fastapi import APIRouter

from apis.version1 import route_jobs
from apis.version1 import route_users
from apis.version1 import route_auth



api_router = APIRouter()

api_router.include_router(route_jobs.router,prefix="/job",tags=["Jobs"])
api_router.include_router(route_users.router,prefix="/users",tags=["Users"])
api_router.include_router(route_auth.router, prefix="/auth", tags=["auth"])