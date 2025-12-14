from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command('help'))
async def help_command_handler(message: Message):
    """Обработчик команды вывода помощи"""

    help_text = (
        'Список команд:\n\n'
        '/start — начать работу и сбросить контекст\n'
        '/help — показать это сообщение\n'
        '/context — показать контекст\n'
        '/stop — остановить бота\n'
    )
    await message.answer(help_text)
