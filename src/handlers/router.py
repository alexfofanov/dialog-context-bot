from aiogram import Router

from src.handlers.start import router as start_router
from src.handlers.stop import router as stop_router


def setup_routers(main_router: Router):
    main_router.include_router(start_router)
    main_router.include_router(stop_router)
