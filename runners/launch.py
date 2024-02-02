from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage
from loguru import logger

from config.config_reader import config

# Определение бота
logger.info("Creating Bot and Dispatcher")

token = config.bot_token.get_secret_value()
storage = RedisStorage.from_url(
    "redis://localhost:6379/0",
)
bot = Bot(token, parse_mode=ParseMode.HTML)
dp_main = Dispatcher(storage=storage)


def startModules():  # Запуск модулей
    try:
        logger.info("Start loading modules...")
        from bot.features.timetable import loader
        from bot.admin import loader
        from bot.core import loader
        from local_socket import server

        logger.info("Modules loading completed!")
    except Exception as e:
        logger.error(f"Error when import: {e}")


startModules()
