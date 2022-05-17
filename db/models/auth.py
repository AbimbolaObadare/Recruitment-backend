from fastapi_users_db_sqlalchemy import declared_attr
from fastapi_users_db_sqlalchemy.access_token import SQLAlchemyBaseAccessTokenTable
from db.base_class import Base
from sqlalchemy import Column, ForeignKey, Integer


class AccessToken(SQLAlchemyBaseAccessTokenTable[int], Base):
    @declared_attr
    def user_id(cls):
        return Column(Integer, ForeignKey("user.id", ondelete="cascade"), nullable=False)
