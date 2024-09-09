from aiogram import Router
from modules.routers.routers import router as root_router

router = Router()

router.include_router(root_router)
