from typing import Any
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    """Creates tablename for database from class name"""

    id: Any
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
