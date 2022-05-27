from typing import Optional
from fastapi_users.authentication.strategy.db import AccessTokenDatabase, DatabaseStrategy

from db.models.auth import AccessToken
from db.session import get_access_token_db, get_user_db

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin

from db.models.users import User
from core.config import settings

from fastapi_users.authentication import AuthenticationBackend, BearerTransport

SECRET = settings.secret_key

bearer_transport = BearerTransport(tokenUrl="auth/login")


def get_database_strategy(
    access_token_db: AccessTokenDatabase[AccessToken] = Depends(get_access_token_db),
) -> DatabaseStrategy:
    return DatabaseStrategy(access_token_db, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_database_strategy,
)


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        # TODO: Add email logic
        print(f"User {user.first_name} has registered.")

    async def on_after_forgot_password(self, user: User, token: str, request: Optional[Request] = None):
        #TODO: Add email logic
        print(f"User {user.first_name} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(self, user: User, token: str, request: Optional[Request] = None):
        #TODO: Add email logic
        print(f"Verification requested for user {user.first_name}. Verification token: {token}")


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
