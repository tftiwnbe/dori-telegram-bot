from aiogram.types import (
    InlineKeyboardButton as IButton,
    InlineKeyboardMarkup as IMarkup,
)


main_kb = [
    [
        IButton(text="Пользователи", callback_data="user_managment"),
        IButton(text="Настройка бота", callback_data="bot_settings"),
    ],
    [
        IButton(text="Программа1", callback_data="program1_settings"),
        IButton(text="Программа2", callback_data="program2_settings"),
    ],
]


main_kb = IMarkup(inline_keyboard=main_kb)
