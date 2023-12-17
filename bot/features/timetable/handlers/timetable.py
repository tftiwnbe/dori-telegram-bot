from aiogram import Router, F
from aiogram.types import CallbackQuery
from loguru import logger

from bot.features.timetable.keyboards import timetable_menu as kb
from bot.features.timetable.convert import convert_timetable
import database.timetable as timetable_db  # Импортируем класс (ещё не изучено)

from bot.features.timetable.notifications import redis

db = timetable_db.Timetable()  # создаём алиас на метод класса?
router = Router()


@router.callback_query(F.data == "timetable")
async def timetable_menu_callback_handler(callback: CallbackQuery) -> None:
    await callback.message.answer(
        "Расписание занятий в Таймырском колледже", reply_markup=kb.sub_kb
    )
    await callback.answer()
    await callback.message.edit_reply_markup()


@router.callback_query(F.data == "convert_timetable")
async def convert_timetable_callback_handler(callback: CallbackQuery) -> None:
    await convert_timetable()
    await callback.answer()


@router.callback_query(F.data == "get_timetable")
async def send_timetable_callback_handler(callback: CallbackQuery) -> None:
    await callback.message.answer_document(redis.get("pdf"))


@router.callback_query(F.data == "subscribe")
async def subscribe_callback_handler(callback: CallbackQuery) -> None:
    user_id = callback.from_user.id
    if not await db.subscribed_user(user_id):
        await db.toggle_user(user_id)
        await callback.message.answer("Вы успешно подписаны\!", reply_markup=kb.get_kb)
        await callback.message.edit_reply_markup()
    else:
        await callback.answer("Вы уже подписаны на обновления расписания :)")

    await callback.answer()


@router.callback_query(F.data == "unsubscribe")
async def unsubscribe_callback_handler(callback: CallbackQuery) -> None:
    user_id = callback.from_user.id
    if await db.subscribed_user(user_id):
        await db.toggle_user(user_id, toggle=0)
        await callback.message.answer(
            "Уведомления отключены\!", reply_markup=kb.menu_kb
        )
        await callback.message.edit_reply_markup()
    else:
        await callback.answer("Вы ничего не изменили, хахах :)")

    await callback.answer()
