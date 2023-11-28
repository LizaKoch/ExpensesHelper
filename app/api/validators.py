from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.category import category_crud


async def check_name_duplicate(
        room_name: str,
        session: AsyncSession,
) -> None:
    room_id = await category_crud.get_category_id_by_name(room_name, session)
    if room_id is not None:
        raise HTTPException(
            status_code=422,
            detail='Такая категория уже существует!',
        )
