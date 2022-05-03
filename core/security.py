from datetime import datetime,timedelta
from typing import Optional
from jose import jwt

from core.config import settings


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Create JWT Token"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.access_token_expire_minutes)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
    return encoded_jwt
