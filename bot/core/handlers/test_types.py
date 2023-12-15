from aiogram import Router, F
from aiogram.types import Message
from loguru import logger

router = Router()


@router.message(F.text)
async def message_with_text(message: Message):
    await message.answer("Это текстовое сообщение!")
    logger.info("Handled text")


@router.message(F.sticker)
async def message_with_sticker(message: Message):
    await message.answer("Это стикер!")
    logger.info("Handled stiker")


@router.message(F.animation)
async def message_with_gif(message: Message):
    await message.answer("Это GIF!")
    logger.info("Handled GIF")
