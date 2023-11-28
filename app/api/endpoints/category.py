from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import check_name_duplicate
from app.core.db import get_async_session
from app.core.user import current_superuser
from app.crud.category import category_crud
from app.schemas.category import CategoryCreate, CategoryDB

router = APIRouter(
    prefix='/categories',
    tags=['Categories'],
)

@router.get(
    '/',
    response_model=list[CategoryDB],
)
async def get_all_categories(
        session: AsyncSession = Depends(get_async_session),
):
    """Get all categories"""
    categories = await category_crud.get_multi(session)
    return categories

@router.post(
    '/',
    response_model=CategoryDB,
    dependencies=[Depends(current_superuser)],
)
async def create_new_ctegory(
        category: CategoryCreate,
        session: AsyncSession = Depends(get_async_session),
):
    """Create new category."""
    await check_name_duplicate(
        category.id, session,
    )
    return await category_crud.create(category, session)
