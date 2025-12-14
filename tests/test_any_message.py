from unittest.mock import AsyncMock

import pytest
from aiogram.types import User, Message

from src.handlers.any_message import any_message_handler


@pytest.mark.asyncio
async def test_amy_message_handler():
    mock_message = AsyncMock(spec=Message)
    mock_message.text = 'Привет!'
    mock_message.answer = AsyncMock()

    mock_user = AsyncMock(spec=User)
    mock_user.id = 123
    mock_message.from_user = mock_user

    fake_histories = {}
    fake_chatgpt_service = AsyncMock()
    fake_chatgpt_service.generate = AsyncMock(return_value='Ответ модели')

    await any_message_handler(
        mock_message,
        conversation_histories=fake_histories,
        chatgpt_service=fake_chatgpt_service,
    )

    fake_chatgpt_service.generate.assert_called_once()
    called_args = fake_chatgpt_service.generate.call_args[0]
    history_passed = called_args[0]
    print(history_passed)
    assert history_passed == [
        {'role': 'user', 'content': 'Привет!'},
        {'role': 'assistant', 'content': 'Ответ модели'},
    ]

    assert fake_histories[123] == [
        {'role': 'user', 'content': 'Привет!'},
        {'role': 'assistant', 'content': 'Ответ модели'},
    ]
