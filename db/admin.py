from sqlalchemy import Boolean, Column, Integer, String

from db.base_class import Base

# TODO: Check of admin model is written well
class Admin(Base):
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String,unique=True,nullable=False)
    is_superuser = Column(Boolean(),default=False)
    hashed_password = Column(String,nullable=False)