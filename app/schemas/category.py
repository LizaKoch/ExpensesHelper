from typing import Optional

from pydantic import BaseModel, validator


class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None


class CategoryUpdate(CategoryBase):
    @validator('name')
    def check_name(cls, value):
        if value is None or not value:
            raise ValueError(
                'Название категории не может быть пустым',
            )
        return value

class CategoryCreate(CategoryUpdate):
    pass

class CategoryDB(CategoryBase):
    id: int

    class Config:
        orm_mode = True
