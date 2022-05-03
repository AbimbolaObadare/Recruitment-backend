from core.hashing import Hasher
from db.models.users import Users
from db.repo.auth import get_user
from db.session import get_db
from fastapi import Depends,HTTPException, status
from schemas.users import UserCreate
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from core.config import settings

from apis.utils import OAuth2PasswordBearerWithCookie

def create_new_user(user: UserCreate, db: Session):
    user = Users(
        username=user.username,
        email=user.email,
        hashed_password=Hasher.get_password_hash(user.password),
        is_applicant=user.is_applicant,
        is_recruiter = user.is_recruiter,
        is_superuser=False,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_email(email: str, db: Session):
    user = db.query(Users).filter(Users.email == email).first()
    return user

 
def authenticate_user(username: str, password: str, db: Session = Depends(get_db)):
    user = get_user(username=username, db=db)
    if not user:
        return False
    if not Hasher.verify_password(password, user.hashed_password):
        return False
    return user


oauth2_scheme = OAuth2PasswordBearerWithCookie(tokenUrl="/auth/token")
    
def get_current_user_from_token(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )
    try:
        payload = jwt.decode(
            token, settings.secret_key, algorithms=[settings.algorithm]
        )
        username: str = payload.get("sub")
        print("username/email extracted is ", username)
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user(username=username, db=db)
    if user is None:
        raise credentials_exception
    return user    