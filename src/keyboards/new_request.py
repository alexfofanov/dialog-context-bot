from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def bottom_keyboard():
    """Клавиатура с кнопкой Новый запрос"""

    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text='Новый запрос')]],
        resize_keyboard=True,
        one_time_keyboard=False,
    )

    return keyboard
