from aiogram import F, Router, types

from src.keyboards.new_request import bottom_keyboard

router = Router()


@router.message(F.text == 'Новый запрос')
async def new_request_handler(
    message: types.Message, conversation_histories: dict[int, list]
):
    await message.delete()
    conversation_histories.pop(message.from_user.id, None)
    await message.answer(
        'Контекст сброшен. Напишите новый запрос:', reply_markup=bottom_keyboard()
    )
