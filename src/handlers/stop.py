from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command('stop'))
async def stop_command_handler(
    message: Message, conversation_histories: dict[int, list[dict[str, str]]]
):
    """Обработчик команды остановки"""

    conversation_histories.pop(message.from_user.id, None)
    await message.answer('Прощай!')
