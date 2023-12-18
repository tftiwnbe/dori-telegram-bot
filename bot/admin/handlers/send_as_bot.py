from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.enums import ParseMode
from aiogram.types import Message
from bot.admin.filters.is_admin import IsAdmin

from runners.launch import bot

import database.user as user_db
import database.admin as admin_db

users_db = user_db.Users()
admin_db = admin_db.Admin()
router = Router()


@router.message(Command("sendall"), IsAdmin())
async def cmd_notify_all(message: Message, command: CommandObject) -> None:
    users = await users_db.id_of_users()
    if command.args is None:
        await message.answer("Ошибка: не переданы аргументы")
        return
    text = command.args
    for user in list(users):
        await bot.send_message(user, f"{text}", parse_mode=ParseMode.HTML)


@router.message(Command("sendphoto"), IsAdmin())
async def cmd_photo_to_all(message: Message) -> None:
    users = await users_db.id_of_users()
    if message.photo is None:
        await message.answer("Ошибка: не переданы аргументы")
        return
    for user in list(users):
        await bot.send_photo(user, message.photo[-1].file_id)


@router.message(Command("sendvideo"), IsAdmin())
async def cmd_video_to_all(message: Message) -> None:
    users = await users_db.id_of_users()
    if message.video is None:
        await message.answer("Ошибка: не переданы аргументы")
        return
    for user in list(users):
        await bot.send_video(user, message.video.file_id)


@router.message(Command("sendadmins"), IsAdmin())
async def cmd_notify_admins(message: Message, command: CommandObject) -> None:
    admins = await admin_db.id_of_admins()
    if command.args is None:
        await message.answer("Ошибка: не переданы аргументы")
        return
    text = command.args
    for admin in list(admins):
        await bot.send_message(admin, f"{text}", parse_mode=ParseMode.HTML)
