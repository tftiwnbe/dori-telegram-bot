from loguru import logger
from bot.admin.handlers import admin_panel, user_management, send_as_bot
from runners.launch import dp_main as dp


def enable() -> None:  # Регестрация Роутеров
    dp.include_routers(admin_panel.router, user_management.router, send_as_bot.router)
    logger.info("Admin routers included")
