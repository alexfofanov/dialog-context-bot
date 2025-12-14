from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from src.keyboards.new_request import bottom_keyboard

router = Router()


@router.message(Command('start'))
async def start_command_handler(
    message: Message,
    conversation_histories: dict[int, list[dict[str, str]]],
):
    """Обработчик команды запуска"""

    conversation_histories.pop(message.from_user.id, None)
    await message.answer('Привет! Введите свой запрос:', reply_markup=bottom_keyboard())
