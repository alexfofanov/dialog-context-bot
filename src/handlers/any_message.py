from aiogram import Router, types

from src.keyboards.new_request import bottom_keyboard
from src.services.openai_service import OpenAIService

router = Router()


@router.message()
async def any_message_handler(
    message: types.Message,
    conversation_histories: dict[int, list[dict[str, str]]],
    chatgpt_service: OpenAIService,
):
    user_id = message.from_user.id
    history = conversation_histories.setdefault(user_id, [])

    history.append({'role': 'user', 'content': message.text})

    answer = await chatgpt_service.generate(
        history, system_prompt='Ты полезный ассистент'
    )

    history.append({'role': 'assistant', 'content': answer})

    await message.answer(answer, reply_markup=bottom_keyboard())
