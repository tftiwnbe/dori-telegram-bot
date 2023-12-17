from aiogram.types import (
    InlineKeyboardButton as IButton,
    InlineKeyboardMarkup as IMarkup,
)


menu_kb = [
    [
        IButton(text="Расписание занятий", callback_data="timetable"),
        IButton(text="Опоздания", callback_data="bad_humans"),
    ],
    [
        IButton(text="Помощь", callback_data="help"),
    ],
]

menu_kb = IMarkup(inline_keyboard=menu_kb)
