import asyncio

# import sys
# import logging

from loguru import logger
from config import loguru
from runners.launch import bot, dp_main as dp

loop = asyncio.get_event_loop()  # Ссылка на текущий цикл событий
logger.info("main.py was imported")


async def on_shutdown(_):
    await bot.session.close()


async def main() -> None:  # Запуск бота
    await bot.delete_webhook(drop_pending_updates=True)
    logger.info("Start Polling")
    await dp.start_polling(bot, skip_updates=True, on_shutdown=on_shutdown)


if __name__ == "__main__":
    # logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    logger.info("Start bot")
    loop.run_until_complete(main())
