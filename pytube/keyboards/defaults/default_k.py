from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

konfeta_keyboard = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text='Начать с начала'),
            KeyboardButton(text='Выйти из игры')
        ]
    ],
    resize_keyboard=True
)