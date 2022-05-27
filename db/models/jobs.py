from datetime import datetime

from db.base_class import Base
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


# TODO: Work on Deleting post automatically on setting date
class Job(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    company = Column(String, nullable=False)
    company_url = Column(String)
    location = Column(String, nullable=False)
    description = Column(String, nullable=False )
    date_posted = Column(DateTime, nullable=False, default=datetime.now)
    # delete_date = Column(DateTime,nullable=False)
    is_active = Column(Boolean, default=True)
    owner = relationship("User", back_populates="jobs")
    owner_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"))
    question = relationship("Question", back_populates="job")
