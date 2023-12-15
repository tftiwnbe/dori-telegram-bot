import aiomysql
from loguru import logger
from main import loop
from config.config_reader import config


@logger.catch
async def connect():  # Возвращает пул соединений с MySQL
    db_pool = await aiomysql.create_pool(
        host=config.db_host.get_secret_value(),
        user=config.db_user.get_secret_value(),
        password=config.db_pass.get_secret_value(),
        db=config.db_name.get_secret_value(),
        autocommit=True,
        pool_recycle=100,
        loop=loop,
    )
    logger.info("Database connected!")
    return db_pool


logger.info("Connecting to database...")
# Остановка выполнения до соединения с БД
db_connect = loop.run_until_complete(connect())
