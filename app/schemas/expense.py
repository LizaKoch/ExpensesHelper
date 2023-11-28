from typing import Optional

from pydantic import BaseModel, validator


class ExpenseBase(BaseModel):
    title: str
    amount: float
    description: Optional[str] = None


class ExpenseUpdate(ExpenseBase):
    @validator('amount')
    def check_amount(cls, value):
        if value <= 0:
            raise ValueError(
                'Сумма расхода не может быть меньше или равна нулю',
            )
        return value

class ExpenseCreate(ExpenseUpdate):
    category_id: int


class ExpenseDB(ExpenseBase):
    id: int
    category_id: int

    class Config:
        """ORM mode."""

        orm_mode = True
