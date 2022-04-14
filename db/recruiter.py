from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from db.base_class import Base


class Recruiter(Base):
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String,unique=True,nullable=False)
    email = Column(String,nullable=False,unique=True,index=True)
    hashed_password = Column(String,nullable=False)
    is_active = Column(Boolean(),default=True)
    jobs = relationship("Job",back_populates="recruiter")
