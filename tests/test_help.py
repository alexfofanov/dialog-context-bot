from unittest.mock import AsyncMock

import pytest
from aiogram.types import User, Message

from src.handlers.help import help_command_handler


@pytest.mark.asyncio
async def test_help_handler():
    mock_message = AsyncMock(spec=Message)
    mock_message.text = '/help'
    mock_message.answer = AsyncMock()

    await help_command_handler(mock_message)

    mock_message.answer.assert_called()

    text_sent = mock_message.answer.call_args[0][0]
    assert 'Вот что я умею:' in text_sent
