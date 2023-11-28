from sqlalchemy import Column, Float, String

from app.core.db import Base


class Statistics(Base):
    total_expenses: float = Column(Float, nullable=False)
    average_expenses: float = Column(Float, nullable=False)
    expenses_by_category: dict[str, float] = Column(String, nullable=False)
