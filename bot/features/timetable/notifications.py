import database.admin as admin_db
import redis
import database.timetable as timetable_db
from aiogram.enums import ParseMode
from aiogram.types import FSInputFile
from loguru import logger
from runners.launch import bot

redis = redis.Redis(host="localhost", port=6379, decode_responses=True)
timetable_db = timetable_db.Timetable()
admin_db = admin_db.Admin()


async def cmd_timetable_send(pdf) -> None:
    users = await timetable_db.id_of_subscribers()

    for user in list(users):
        await bot.send_document(user, pdf)


async def cmd_notify_admins(text) -> None:
    admins = await admin_db.id_of_admins()

    for admin in list(admins):
        await bot.send_message(admin, text, parse_mode=ParseMode.HTML)


async def save_pdf(pdf):
    admins = await admin_db.id_of_admins()
    try:
        converted_pdf = FSInputFile("/home/dori/bot/features/timetable/Расписание.pdf")
        for admin in list(admins):
            pdf = await bot.send_document(admin, converted_pdf)
        pdf_id = pdf.document.file_id
        redis.set(name="pdf", value=pdf_id)
        return await cmd_timetable_send(pdf_id)
    except Exception as e:
        logger.error(f"Save pdf error: {e}")
        await cmd_notify_admins(
            f"""
        Ошибка при сохранении pdf!

        {e}
        """
        )
