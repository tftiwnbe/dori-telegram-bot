from aiogram.types import (
    InlineKeyboardButton as IButton,
    InlineKeyboardMarkup as IMarkup,
)

menu_kb = [
    [IButton(text="Статистика", callback_data="users_statistic")],
    [
        IButton(text="Пользователи", callback_data="users_list"),
        IButton(text="Администраторы", callback_data="admins_list"),
    ],
    [IButton(text=" <-- Вернуться", callback_data="admin_menu")],
]

users_kb = [
    [IButton(text="Статистика", callback_data="users_statistic")],
    [
        IButton(text="Список пользователей", callback_data="users_list"),
    ],
    [IButton(text=" <-- Вернуться", callback_data="admin_menu")],
]

admins_kb = [
    [IButton(text="Статистика", callback_data="users_statistic")],
    [
        IButton(text="Список Администраторов", callback_data="admins_list"),
    ],
    [IButton(text=" <-- Вернуться", callback_data="admin_menu")],
]

stats_kb = [
    [
        IButton(text="Пользователи", callback_data="users_list"),
        IButton(text="Администраторы", callback_data="admins_list"),
    ],
    [IButton(text=" <-- Вернуться", callback_data="admin_menu")],
]


menu_kb = IMarkup(inline_keyboard=menu_kb)
users_kb = IMarkup(inline_keyboard=users_kb)
admins_kb = IMarkup(inline_keyboard=admins_kb)
stats_kb = IMarkup(inline_keyboard=stats_kb)
