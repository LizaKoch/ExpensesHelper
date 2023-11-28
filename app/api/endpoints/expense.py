from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import User, current_user
from app.schemas.expense import ExpenseCreate, ExpenseDB

router = APIRouter(
    prefix='/expenses',
    tags=['Expenses'],
)

@router.get(
    '/my_expenses',
    response_model=list[ExpenseDB],
    response_model_exclude_none=True,
)
async def get_my_expenses(
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user),
):
    """Получение списка расходов текущего пользователя"""
    expenses = await expense_crud.get_multi(session, user.id)
    return expenses

@router.post(
    '/',
    response_model=ExpenseDB,
)
async def create_expense(
        expense: ExpenseCreate,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user),
):
    """Создание расхода"""
    new_expense = await expense_crud.create(expense, session, user)
    return new_expense
