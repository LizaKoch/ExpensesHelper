from sqlalchemy import Column, DateTime, Float, ForeignKey, String, Integer

from app.core.db import Base


class Expense(Base):
    name: str = Column(String, nullable=False)
    amount: float = Column(Float, nullable=False)
    date: str = Column(DateTime, nullable=False)
    category_id: str = Column(String, ForeignKey('category.id', name='category_id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id', name='user_id'), nullable=False)
    description: str = Column(String, nullable=True)
