import asyncio
from typing import Callable, Awaitable, Dict, Any
from aiogram import BaseMiddleware
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.types import TelegramObject, CallbackQuery
from loguru import logger
from aiogram.dispatcher.flags import extract_flags, get_flag


class ThrottlingMiddleware(BaseMiddleware):
    def __init__(  # Инициализация: принимаем экземпляр хранилища и время антифлуда
        self, storage: RedisStorage, rate_limit: int = 1, key_prefix="antiflood_"
    ) -> None:
        self.storage = storage
        self.rate_limit = rate_limit
        self.prefix = key_prefix

    async def __call__(  # хэндлер - ловим объекты, ивент - объект события, дата - содержимое объекта
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        # Закготовленные реплики
        too_many_request = "Я обнаружила подозрительную активность, вы наказаны, бугага"
        unlocked = "Ладно, всё хорошо :\)"

        # Ищем отмеченные флагом хэндлеры
        marked = get_flag(data, "rate_limit")
        logger.debug(marked)
        if marked:
            limit = marked
        else:  # Если хэндлер не отмечен - используем стандартные значения
            limit = self.rate_limit

        if isinstance(event, CallbackQuery):
            key = f"{self.prefix}_{event.data}__message__from__{event.from_user.id}"
        else:
            key = f"{self.prefix}_{event.text}__message__from__{event.from_user.id}"

        """
        Получаем из редиски "ключ", если он существует
        Если не существует, то добавляем ега равным 1 и пропускаем хэндлер
        Если "ключ" сообщения равен 1, блокируем хэнлер, возвращая пустоту
        """
        message = await self.storage.redis.get(name=key)

        if message:
            if int(message.decode()) == 1:
                await self.storage.redis.set(name=key, value=0, ex=limit)
                if isinstance(event, CallbackQuery):  # Колбэки обрабатываем иначе
                    await event.answer()
                    # await event.message.edit_reply_markup()
                    await event.message.answer(too_many_request)
                    await asyncio.sleep(limit)
                    return await event.message.answer(unlocked)
                else:
                    await event.answer(too_many_request)
                    await asyncio.sleep(limit)
                    return await event.answer(unlocked)
            return

        await self.storage.redis.set(name=key, value=1, ex=limit)

        return await handler(event, data)

    logger.info("ThrottlingMiddleware ready")
