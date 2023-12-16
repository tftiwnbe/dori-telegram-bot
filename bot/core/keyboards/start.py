from aiogram.types import (
    InlineKeyboardButton as IButton,
    InlineKeyboardMarkup as IMarkup,
)


new_start_kb = [
    [
        IButton(text="Познакомимся!", callback_data="start_meet"),
        IButton(text="Главное меню", callback_data="main_menu"),
    ]
]
old_start_kb = [
    [
        IButton(text="Расскажи о себе", callback_data="start_meet"),
        IButton(text="Главное меню ->", callback_data="main_menu"),
    ]
]

new_start_kb = IMarkup(inline_keyboard=new_start_kb)
old_start_kb = IMarkup(inline_keyboard=old_start_kb)
