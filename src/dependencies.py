
from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
from aiohttp import ClientSession

from src.config import TELEGRAM_BOT_TOKEN


class Dependencies:
    """Зависимости приложения"""

    def __init__(self) -> None:
        self.session: ClientSession | None = None
        self.bot: Bot | None = None
        self.dp: Dispatcher | None = None

    async def init(self) -> None:
        self.session = AiohttpSession(timeout=30)
        self.bot = Bot(token=TELEGRAM_BOT_TOKEN, session=self.session)
        self.dp = Dispatcher(bot=self.bot, session=self.session)

    async def close(self) -> None:
        if self.bot:
            await self.bot.session.close()

        # закрываем сессию
        if self.session:
            await self.session.close()
