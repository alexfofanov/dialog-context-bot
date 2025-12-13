from aiogram import Router

from src.handlers.any_message import router as any_message_router
from src.handlers.context import router as get_context_router
from src.handlers.help import router as help_router
from src.handlers.new_request import router as new_request_router
from src.handlers.start import router as start_router
from src.handlers.stop import router as stop_router


def setup_routers(main_router: Router):
    """Подключение роутеров"""

    main_router.include_router(start_router)
    main_router.include_router(stop_router)
    main_router.include_router(help_router)
    main_router.include_router(new_request_router)
    main_router.include_router(get_context_router)
    main_router.include_router(any_message_router)
