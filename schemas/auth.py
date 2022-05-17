from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    first_name: str
    last_name: str
    is_applicant: bool = False
    is_recruiter: bool = False


class UserCreate(schemas.BaseUserCreate):
    first_name: str
    last_name: str
    is_applicant: bool = False
    is_recruiter: bool = False


class UserUpdate(schemas.BaseUserUpdate):
    pass
