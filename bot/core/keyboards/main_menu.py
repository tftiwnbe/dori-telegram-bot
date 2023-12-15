from aiogram.types import (
    InlineKeyboardButton as IButton,
    InlineKeyboardMarkup as IMarkup,
)


menu_kb = [
    [
        IButton(text="Программа1", callback_data="program1"),
        IButton(text="Программа2", callback_data="program2"),
    ],
    [
        IButton(text="Помощь", callback_data="help"),
    ],
]

menu_kb = IMarkup(inline_keyboard=menu_kb)
