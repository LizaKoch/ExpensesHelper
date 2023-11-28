from sqlalchemy import Column, DateTime, Float, ForeignKey, String

from app.core.db import Base


class Expense(Base):
    name: str = Column(String, nullable=False)
    amount: float = Column(Float, nullable=False)
    date: str = Column(DateTime, nullable=False)
    category: str = Column(String, ForeignKey('category.name'), nullable=False)
    notes: str = Column(String, nullable=True)
