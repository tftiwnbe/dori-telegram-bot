# import sys
# import logging
from loguru import logger

from config import loguru
from main import loop
from runners.launch import bot
from runners.launch import dp_main as dp


async def on_shutdown():
    from database.connect import close_connection

    await close_connection()


async def main() -> None:  # Запуск бота
    # dp.startup.register(on_startup)
    # dp.shutdown.register(on_shutdown)

    await bot.delete_webhook(drop_pending_updates=True)
    logger.info("Start Polling")
    await dp.start_polling(bot, skip_updates=True, on_shutdown=on_shutdown)


if __name__ == "__main__":
    # logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    logger.info("Start bot")
    loop.run_until_complete(main())
