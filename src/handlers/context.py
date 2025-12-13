from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command('context'))
async def context_handler(
    message: Message,
    conversation_histories: dict[int, list[dict[str, str]]],
):
    """Обработчик команды получения контекста"""

    user_id = message.from_user.id

    history = conversation_histories.get(user_id)

    if not history:
        await message.answer('Контекст пуст — вы ещё не начали диалог.')
        return

    recent_history = history[-10:]
    formatted = []
    for i, turn in enumerate(recent_history, start=1):
        role = turn.get('role', 'unknown')
        text = turn.get('content', '')
        formatted.append(f'{i}. *{role}*: {text}')

    response = '\n'.join(formatted)

    await message.answer(f'📜 *Текущий контекст:*\n{response}', parse_mode='Markdown')
