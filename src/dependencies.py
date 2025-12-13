from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
from aiohttp import ClientSession
from openai import AsyncOpenAI

from src.config import OPENAI_API_KEY, OPENAI_MODEL, TELEGRAM_BOT_TOKEN
from src.services.openai_service import OpenAIService


class Dependencies:
    """Зависимости приложения"""

    def __init__(self) -> None:
        self.session: ClientSession | None = None
        self.bot: Bot | None = None
        self.dp: Dispatcher | None = None
        self.conversation_histories: dict[int, list[dict[str, str]]] = {}
        self.openai_client: AsyncOpenAI | None = None
        self.chatgpt_service: OpenAIService | None = None

    async def init(self) -> None:
        self.session = AiohttpSession(timeout=30)
        self.bot = Bot(token=TELEGRAM_BOT_TOKEN, session=self.session)
        self.openai_client = AsyncOpenAI(api_key=OPENAI_API_KEY)
        self.chatgpt_service = OpenAIService(
            client=self.openai_client, model=OPENAI_MODEL
        )

        self.dp = Dispatcher(
            bot=self.bot,
            session=self.session,
            conversation_histories=self.conversation_histories,
            chatgpt_service=self.chatgpt_service,
        )

    async def close(self) -> None:
        if self.openai_client:
            await self.openai_client.close()

        if self.bot:
            await self.bot.session.close()

        if self.session:
            await self.session.close()
