from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import Category
from app.models.category import Category


class CRUDRCategory(CRUDBase):
    async def get_category_id_by_name(self, category_name: str, session: AsyncSession ) -> Optional[int]:
        db_category_id = await session.execute(select(Category.id).where(Category.name == category_name))
        db_category_id = db_category_id.scalars().first()
        return db_category_id

category_crud = CRUDRCategory(Category)
# теперь в файле с CRUD-методами(эндпоинтами) есть объект reservation_crud (можно использовать методы объекта reservation_crud)

