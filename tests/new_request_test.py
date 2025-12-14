from unittest.mock import AsyncMock

import pytest
from aiogram.types import User, Message

from src.handlers.new_request import new_request_handler
from src.keyboards.new_request import bottom_keyboard


@pytest.mark.asyncio
async def test_new_request_handler():
    mock_message = AsyncMock(spec=Message)
    mock_message.text = 'Новый запрос'
    mock_message.answer = AsyncMock()
    mock_message.delete = AsyncMock()

    mock_user = AsyncMock(spec=User)
    mock_user.id = 456
    mock_message.from_user = mock_user

    fake_histories = {456: [{'role': 'assistant', 'content': 'контент'}]}

    await new_request_handler(mock_message, conversation_histories=fake_histories)

    mock_message.delete.assert_called_once()

    assert 456 not in fake_histories

    mock_message.answer.assert_called_once()

    sent_text = mock_message.answer.call_args[0][0]
    assert 'Контекст сброшен' in sent_text
    assert 'Напишите новый запрос' in sent_text

    kwargs = mock_message.answer.call_args.kwargs
    assert 'reply_markup' in kwargs
    assert isinstance(kwargs['reply_markup'], type(bottom_keyboard()))
