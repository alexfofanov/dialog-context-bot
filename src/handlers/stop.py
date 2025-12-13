from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command('stop'))
async def stop_command_handler(message: Message):
    await message.answer('Прощай!')
