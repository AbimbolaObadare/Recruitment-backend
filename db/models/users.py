from email.policy import default
from fastapi_users.db import SQLAlchemyBaseUserTable
from db.base_class import Base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship


class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String)
    is_applicant = Column(Boolean, nullable=False)
    is_recruiter = Column(Boolean, nullable=False)
    jobs = relationship("Job", back_populates="owner")
