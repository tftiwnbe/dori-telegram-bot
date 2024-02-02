from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery, Message
from loguru import logger
# from aiogram import flags

import database.user as user_db  # Импортируем класс (ещё не изучено)
from bot.core.keyboards import start
from bot.core.say import about_self

global db
db = user_db.Users()  # создаём алиас на метод класса?
router = Router()


@router.message(CommandStart())  # Ловим команду '/start'
# @flags.rate_limit(rate=10, key="start") # Пример применения троттлинг мидлвари
async def command_start_handler(message: Message) -> None:
    user = message.from_user
    logger.info("Start command handled!")
    if await db.search_user(user.id):
        await message.answer("С возвращением!")
        logger.info("That is returned user")
        await message.answer(
            "Чем я могу тебе помочь?", reply_markup=start.old_start_kb
        )
    else:
        await db.add_user(user)  # Добовлем пользователя в БД, если его там нет
        await message.answer(f"Привет, {user.first_name}! Добро пожаловать!")
        logger.info("That is new user")
        await message.answer(
            "Чем я могу тебе помочь?", reply_markup=start.new_start_kb
        )


@router.callback_query(F.data == "start_meet")
async def start_meeting_handler(callback: CallbackQuery) -> None:
    await callback.message.edit_text(
        await about_self(), reply_markup=start.old_start_kb
    )
    await callback.answer()
