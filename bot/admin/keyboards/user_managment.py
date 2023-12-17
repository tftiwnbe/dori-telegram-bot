from aiogram.types import (
    InlineKeyboardButton as IButton,
    InlineKeyboardMarkup as IMarkup,
)

main_kb = [
    [IButton(text="Статистика", callback_data="users_statistic")],
    [
        IButton(text="Список пользователей", callback_data="users_list"),
        IButton(text="Список Администраторов", callback_data="admins_list"),
    ],
    [IButton(text=" <-- Вернуться", callback_data="admin_menu")],
]

main_kb = IMarkup(inline_keyboard=main_kb)
