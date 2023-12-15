from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.exceptions import TelegramBadRequest
from loguru import logger
from contextlib import suppress

from bot.core.keyboards import main_menu

router = Router()


@router.message(F.text.lower() == "/menu")
@router.message(F.text.lower() == "меню")
async def main_menu_text_handler(message: Message) -> None:
    await message.answer("📍 Главное меню", reply_markup=main_menu.menu_kb)


@router.callback_query(F.data == "main_menu")
async def main_menu_callback_handler(callback: CallbackQuery) -> None:
    await callback.message.answer("📍 Главное меню", reply_markup=main_menu.menu_kb)
    await callback.answer()
    await callback.message.edit_reply_markup()


@router.callback_query(F.data)
async def weird_data_handler(callback: CallbackQuery) -> None:
    with suppress(TelegramBadRequest):
        await callback.message.delete()
        await callback.message.answer("Простите, что\-то не так :\(")
        await callback.message.answer(
            "Но вот\.\.\. \n\n📍 Главное меню", reply_markup=main_menu.menu_kb
        )
        logger.warning(
            f"""
            Handled weird data: "{callback.data}"
            by: {callback.from_user.id} - {callback.from_user.username}"""
        )


@router.message()
async def weird_text_handler(message: Message) -> None:  # ловим остальные сообщения
    await message.delete()
    await message.answer(
        "Прости, но я тебя не понимаю :\(",
    )
    await message.answer(
        "Лучше посмотри на моё\.\.\. \n\n📍 Главное меню",
        reply_markup=main_menu.menu_kb,
    )
    logger.warning(
        f"""
        Handled weird text: "{message.text}"
        by: {message.from_user.id} - {message.from_user.username}"""
    )
