import logging

from aiolimiter import AsyncLimiter
from openai import (
    APIConnectionError,
    APIError,
    APITimeoutError,
    AsyncOpenAI,
    RateLimitError,
)

from src.config import OPENAI_MODEL

logger = logging.getLogger(__name__)

OPENAI_FREE_TIER_MAX_RATE = 3


class OpenAIService:
    """Сервис для общения с OpenAI с таймаутами, ретраями и обработкой ошибок"""

    def __init__(self, client: AsyncOpenAI, model: str = OPENAI_MODEL) -> None:
        self.client = client
        self.model = model
        self._limiter = AsyncLimiter(max_rate=OPENAI_FREE_TIER_MAX_RATE, time_period=60)

    async def generate(
        self,
        history: list[dict[str, str]],
        system_prompt: str = None,
        *,
        timeout: float = 30.0,
        max_retries: int = 3,
    ) -> str | None:
        """Генерация ответа с таймаутом и retry"""

        async with self._limiter:
            messages: list[dict[str, str]] = []

            if system_prompt:
                messages.append({'role': 'system', 'content': system_prompt})
            messages.extend(history)

            try:
                response = await self.client.with_options(
                    timeout=timeout, max_retries=max_retries
                ).chat.completions.create(model=self.model, messages=messages)

                answer = response.choices[0].message.content.strip()
                return answer

            except RateLimitError as err:
                logger.warning(f'Rate limit hit (429): {err}')
                return 'Слишком много запросов к API. Пожалуйста, подождите и попробуйте снова.'

            except APITimeoutError as err:
                logger.error(f'Timeout error: {err}')
                return 'Запрос к API занял слишком много времени.'

            except APIConnectionError as err:
                logger.error(f'Connection error: {err}')
                return 'Не удалось подключиться к API.'

            except APIError as err:
                logger.error(f'API returned error: {err}')
                return 'Ошибка от сервера API.'

            except Exception as err:
                logger.exception(f'Unexpected error in OpenAI request: {err}')
                return 'Неожиданная ошибка при общении с OpenAI.'
