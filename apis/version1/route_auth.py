from fastapi import APIRouter
from fastapi_users import FastAPIUsers

from db.models.users import User
from db.repo.auth import get_user_manager, auth_backend
from schemas.auth import UserRead, UserCreate


router = APIRouter()


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)


router.include_router(
    fastapi_users.get_auth_router(auth_backend),
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
)


router.include_router(
    fastapi_users.get_reset_password_router(),
)
current_user = fastapi_users.current_user()
