from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel


class JobBase(BaseModel):
    """Base Model For Jobs"""

    title: Optional[str] = None
    company: Optional[str] = None
    company_url: Optional[str] = None
    location: Optional[str] = "Remote"
    description: Optional[str] = None
    date_posted: Optional[date] = datetime.utcnow().date()


class ShowJob(JobBase):
    "response format for showing jobs"
    title: str
    company: str
    company_url: Optional[str]
    location: str
    date_posted: date
    description: Optional[str]
    is_active: bool

    class Config:  # to convert non dict obj to json
        orm_mode = True


# this will be used to validate data while creating a Job
class JobCreate(JobBase):
    title: str
    company: str
    location: str
    description: str
    is_active: bool = False
