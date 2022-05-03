from db.base_class import Base
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship


class Users(Base):
    """Model for users that a manage the website"""
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    is_recruiter = Column(Boolean(),default=False)
    is_applicant = Column(Boolean(),default=False)
    is_superuser = Column(Boolean(),default=False)
    hashed_password = Column(String,nullable=False)
    jobs = relationship("Job", back_populates="owner")