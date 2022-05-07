from datetime import timedelta

from core.config import settings
from core.security import create_access_token
from db.repo.users import authenticate_user
from db.session import get_db
from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from schemas.token import Token
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/token", response_model=Token)
def login_for_access_token(
    response: Response,
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    """Login function creates access token with jwt and cookies"""
    user = authenticate_user(username=form_data.username, password=form_data.password, db=db)
    """Authentication is done by email"""
    print(user.email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    access_token = create_access_token(data={"sub": user.email}, expires_delta=access_token_expires)
    response.set_cookie(
        key="access_token",
        value=f"Bearer {access_token}",
        httponly=True,
        expires=settings.access_token_expire_minutes,
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/forgot-password")
def forgot_password():
    # Check if email
    return "forgot password"
