from fastapi import APIRouter

from app.api.endpoints import category_router, expense_router, user_router

main_router = APIRouter()
main_router.include_router(expense_router)
main_router.include_router(category_router)
main_router.include_router(user_router)
