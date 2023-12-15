from loguru import logger

logger.add(
    "./logs/main.log",
    rotation="1 week",
    compression="zip",
    colorize=True,
    format="{time:YYYY-MM-DD at HH:mm:ss} | <level>{level}</level> | <level>{message}</level>",
    level="INFO",
)

logger.add(
    "./logs/warnings.log",
    rotation="1 week",
    compression="zip",
    colorize=True,
    format="{time:YYYY-MM-DD at HH:mm:ss} | <level>{level}</level> | <level>{message}</level>",
    level="WARNING",
)
