from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .callback_data import start_callback, konfeta_callback, calc_callback, vsbot, vsplayer, youtube_callback

start_ik = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Скачать видео с Youtube',
                             callback_data=youtube_callback.new())
    ],
    [
        InlineKeyboardButton(text='Сыграть в конфеты',
                             callback_data=konfeta_callback.new())
    ],
    [
        InlineKeyboardButton(text='Калькулятор',
                             callback_data=calc_callback.new())
    ]
])

konfeta_levels_ik = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='vs Player',
                             callback_data=vsplayer.new()),
        InlineKeyboardButton(text='vs Bot',
                             callback_data=vsbot.new())
    ]

    ]
)