from aiogram.types import (
    InlineKeyboardButton as IButton,
    InlineKeyboardMarkup as IMarkup,
)


main_kb = [
    [
        IButton(text="Пользователи", callback_data="user_managment"),
        IButton(text="Настройка бота", callback_data="bot_settings"),
    ],
    [IButton(text="Сконвертировать расписание", callback_data="convert_timetable")],
    [IButton(text="Помощь", callback_data="admin_help")],
]


main_kb = IMarkup(inline_keyboard=main_kb)
