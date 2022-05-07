from datetime import datetime

from db.base_class import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship


# TODO: Work on Deleting post automatically on setting date
class Job(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    company = Column(String, nullable=False)
    company_url = Column(String)
    location = Column(String, nullable=False)
    description = Column(String)
    date_posted = Column(DateTime, nullable=False, default=datetime.utcnow())
    # delete_date = Column(DateTime,nullable=False)
    is_active = Column(Boolean, default=True)
    owner = relationship("Users", back_populates="jobs")
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
