from aiogram.types import (
    InlineKeyboardButton as IButton,
    InlineKeyboardMarkup as IMarkup,
)


subscribe_kb = [
    [
        IButton(text="Подписаться", callback_data="subscribe"),
        IButton(text="Отписаться", callback_data="unsubscribe"),
    ],
    [
        IButton(text="Покажи расписание", callback_data="get_timetable"),
    ],
    [
        IButton(text="Главное меню", callback_data="main_menu"),
    ],
]

timetable_kb = [
    [
        IButton(text="Покажи расписание", callback_data="get_timetable"),
    ],
    [
        IButton(text="Главное меню", callback_data="main_menu"),
    ],
]


menu_kb = [[IButton(text="Главное меню", callback_data="main_menu")]]

sub_kb = IMarkup(inline_keyboard=subscribe_kb)
get_kb = IMarkup(inline_keyboard=timetable_kb)
menu_kb = IMarkup(inline_keyboard=menu_kb)
