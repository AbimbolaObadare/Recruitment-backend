from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db.base_class import Base

# TODO: Fix relationship with Job Model
class Recruitee(Base):
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String,unique=True,nullable=False)
    email = Column(String,nullable=False,unique=True,index=True)
    hashed_password = Column(String,nullable=False)
    