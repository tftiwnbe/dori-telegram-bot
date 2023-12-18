from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from loguru import logger
from bot.admin.filters.is_admin import IsAdmin
from bot.admin.keyboards import admin_panel

router = Router()


@router.message(F.text.lower() == "/.", IsAdmin())
@router.message(F.text.lower() == "/admin", IsAdmin())  # Открыть админку
async def admin_menu_handler(message: Message) -> None:
    await message.delete()
    await message.answer("*Панель администратора:*", reply_markup=admin_panel.main_kb)


@router.callback_query(F.data == "admin_menu", IsAdmin())
async def back_to_admin_menu_handler(callback: CallbackQuery) -> None:
    await callback.message.edit_text(
        "*Панель администратора:*", reply_markup=admin_panel.main_kb
    )
    await callback.answer()
    # await callback.message.edit_reply_markup()
