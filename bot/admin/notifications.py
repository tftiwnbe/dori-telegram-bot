import database.admin as admin_db
from aiogram.enums import ParseMode
from runners.launch import bot

admin_db = admin_db.Admin()


async def notify_admin(text: str) -> None:
    admins = await admin_db.id_of_admins()

    for admin in list(admins):
        await bot.send_message(admin, text, parse_mode=ParseMode.HTML)
