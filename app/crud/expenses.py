from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.expense import Expense
from app.schemas.expense import ExpenseCreate, ExpenseUpdate
from app.models import User


class CRUDExpense(CRUDBase):
    async def get_expenses_by_date(
            self,
            user: User,
            from_date: Optional[str] = None,
            to_date: Optional[str] = None,
            session: AsyncSession = None,
    ):
        expenses = await session.execute(
            select(Expense).where(
                Expense.user_id == user.id,
            ),
        )
        expenses = expenses.scalars().all()
        return expenses
    async def get_by_user(
            self, session: AsyncSession, user: User,
    ):
        expenses = await session.execute(
            select(Expense).where(
                Expense.user_id == user.id,
            ),
        )
        expenses = expenses.scalars().all()
        return expenses


expense_crud = CRUDExpense(Expense)
