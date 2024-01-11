from loguru import logger

from bot.core.middlewares.throttling import ThrottlingMiddleware
from runners.launch import dp_main as dp
from bot.core.handlers import start, main_menu
from runners.launch import storage


def enable() -> None:  # Регестрация Роутеров
    dp.message.middleware(ThrottlingMiddleware(storage))
    # dp.callback_query.middleware(ThrottlingMiddleware(storage))
    dp.include_routers(start.router, main_menu.router)
    logger.info("Core routers included")


enable()
