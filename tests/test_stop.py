from unittest.mock import AsyncMock

import pytest
from aiogram.types import User, Message

from src.handlers.stop import stop_command_handler


@pytest.mark.asyncio
async def test_stop_handler():
    mock_message = AsyncMock(spec=Message)
    mock_message.text = '/stop'
    mock_message.answer = AsyncMock()

    mock_user = AsyncMock(spec=User)
    mock_user.id = 123
    mock_message.from_user = mock_user

    fake_histories = {}

    await stop_command_handler(mock_message, conversation_histories=fake_histories)

    mock_message.answer.assert_called()

    text_sent = mock_message.answer.call_args[0][0]
    assert 'Прощай!' in text_sent
