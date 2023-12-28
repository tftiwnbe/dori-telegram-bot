import asyncio
# import logging
# import sys

from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web
from loguru import logger

from config import loguru
from config.config_reader import config
from runners.launch import bot
from runners.launch import dp_main as dp

HOST = config.web_server_host.get_secret_value()
PORT = int(config.web_server_port.get_secret_value())
URL = config.base_webhook_url.get_secret_value()
PATH = "/webhook"

loop = asyncio.get_event_loop()  # Ссылка на текущий цикл событий
logger.info("main.py was imported")


async def on_startup(bot) -> None:
    await bot.set_webhook(f"{URL}{PATH}")


async def on_shutdown(_):
    await bot.session.close()


def main() -> None:  # Запуск бота
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    app = web.Application()
    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
    )
    webhook_requests_handler.register(app, path=PATH)

    setup_application(app, dp, bot=bot)
    web.run_app(app, loop=loop, host=HOST, port=PORT)

    logger.info("Start Webhook")


if __name__ == "__main__":
    # logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    logger.info("Start bot")
    main()
