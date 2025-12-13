import asyncio

from aiogram import Dispatcher

from src.dependencies import Dependencies
from src.handlers.router import setup_routers
from src.logger import setup_logging


async def main():
    setup_logging()
    deps = Dependencies()
    await deps.init()

    dp: Dispatcher = deps.dp

    setup_routers(dp)

    try:
        await dp.start_polling(deps.bot)
    finally:
        await deps.close()


if __name__ == '__main__':
    asyncio.run(main())
