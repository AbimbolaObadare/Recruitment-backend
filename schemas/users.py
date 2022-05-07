from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    is_recruiter: bool = False
    is_applicant: bool = False
    password: str


class UserShow(BaseModel):
    username: str
    email: EmailStr
    is_recruiter: bool
    is_applicant: bool

    class Config:  # to convert non dict obj to json
        orm_mode = True
