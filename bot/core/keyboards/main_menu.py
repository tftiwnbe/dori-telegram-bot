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
        IButton(text="Помощь", callback_data="help_menu"),
    ],
]

help_kb = [
    [
        IButton(text="<--Главное меню", callback_data="main_menu"),
        IButton(text="Связь с богами", callback_data="say_to_admin"),
    ],
]

menu_kb = IMarkup(inline_keyboard=menu_kb)
help_kb = IMarkup(inline_keyboard=help_kb)
