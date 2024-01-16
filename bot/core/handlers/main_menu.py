from aiogram import Router, F
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.exceptions import TelegramBadRequest
from loguru import logger
from contextlib import suppress

from runners.launch import dp_main
from bot.core.keyboards import main_menu
from bot.core.help import help_say

router = Router()


@dp_main.message(F.text.lower() == "/menu")
@dp_main.message(F.text.lower() == "меню")
async def main_menu_text_handler(message: Message, state: FSMContext) -> None:
    if not await state.get_state():
        await message.delete()
        await message.answer("📍 Главное меню", reply_markup=main_menu.menu_kb)
    else:
        await message.delete()
        await state.clear()
        await message.answer(
            "Активность прерванна\!", reply_markup=ReplyKeyboardRemove()
        )
        await message.answer("Назад\! В главное меню\!", reply_markup=main_menu.menu_kb)


@dp_main.message(F.text.lower() == "/cancel")
@dp_main.message(F.text.lower() == "отмена")
async def cmd_cancel(message: Message, state: FSMContext):
    if not await state.get_state():
        await message.answer(text="Нечего отменять", reply_markup=ReplyKeyboardRemove())
    else:
        await state.clear()
        await message.answer("Действие отменено", reply_markup=ReplyKeyboardRemove())
        await message.answer(
            "Возвращаемся в главное меню", reply_markup=main_menu.menu_kb
        )


@dp_main.callback_query(F.data == "main_menu")
async def main_menu_callback_handler(callback: CallbackQuery) -> None:
    await callback.message.edit_text("📍 Главное меню", reply_markup=main_menu.menu_kb)
    await callback.answer()


@dp_main.callback_query(F.data == "exit_from_menu")
async def exit_from_menu_callback_handler(callback: CallbackQuery) -> None:
    await callback.message.edit_text("📍 Главное меню", reply_markup=main_menu.menu_kb)
    await callback.answer()


@router.callback_query(F.data == "help_menu")
async def help_menu_callback_handler(callback: CallbackQuery) -> None:
    await callback.message.edit_text(await help_say(), reply_markup=main_menu.help_kb)


@router.callback_query(F.data)
async def weird_data_handler(callback: CallbackQuery) -> None:
    with suppress(TelegramBadRequest):
        # await callback.message.delete()
        await callback.message.edit_text("Простите, что\-то не так :\(")
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
