import database.timetable as timetable_db
import redis
from loguru import logger
from runners.launch import bot
from bot.admin.notifications import notify_admin
from aiogram.types import FSInputFile

timetable_db = timetable_db.Timetable()
redis = redis.Redis(host="localhost", port=6379, decode_responses=True)


async def notify_timetable_subs():
    users = await timetable_db.id_of_subscribers()
    try:
        converted_pdf = FSInputFile("/home/dori/bot/features/timetable/Расписание.pdf")
        pdf = await bot.send_document(list(users)[0], converted_pdf)
        pdf_id = pdf.document.file_id
        redis.set(name="pdf", value=pdf_id)
        for user in list(users)[1:]:
            pdf = await bot.send_document(user, pdf_id)
    except Exception as e:
        logger.error(f"Save pdf error: {e}")
        await notify_admin(
            f"""
        Ошибка при сохранении pdf!

        {e}
        """
        )
