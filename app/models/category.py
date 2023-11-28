from sqlalchemy import Column, String

from app.core.db import Base


class Category(Base):
    name: str = Column(String, nullable=False)
    description: str = Column(String, nullable=True)
