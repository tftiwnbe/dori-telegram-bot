# import logging
# import sys
import asyncio

from loguru import logger

loop = asyncio.get_event_loop()  # Ссылка на текущий цикл событий


def read_configs():
    from config.config_reader import config

    global HOST
    global PORT
    global URL
    global PATH

    HOST = config.web_server_host.get_secret_value()
    PORT = int(config.web_server_port.get_secret_value())
    URL = config.base_webhook_url.get_secret_value()
    PATH = "/aiogram"


async def on_startup(bot) -> None:
    await bot.set_webhook(f"{URL}{PATH}")


async def on_shutdown():
    from database.connect import close_connection

    await close_connection()


def main() -> None:  # Запуск бота
    from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
    from aiohttp import web

    from config import loguru
    from runners.launch import bot
    from runners.launch import dp_main as dp

    read_configs()
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    app = web.Application()
    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
    )
    webhook_requests_handler.register(app, path=PATH)

    logger.info("Start catching Webhooks")
    setup_application(app, dp, bot=bot)
    web.run_app(app, loop=loop, host=HOST, port=PORT)


if __name__ == "__main__":
    # logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    logger.info("Start bot")
    main()
