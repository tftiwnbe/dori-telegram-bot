from bot.features.timetable.handlers import timetable

from loguru import logger
from runners.launch import dp_main as dp


def enable() -> None:  # Регестрация Роутеров
    dp.include_routers(timetable.router)
    logger.info("Timetable routers included")
