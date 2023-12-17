from aiogram.filters import BaseFilter
from aiogram.types import Message
from loguru import logger
import database.admin as admin_db  # Импортируем класс (ещё не изучено)

global db
db = admin_db.Admin()


class IsAdmin(BaseFilter):  # наш класс наследует свойства от BaseFilter
    async def __call__(self, message: Message) -> bool:  # магический метод?
        admin_list = await db.id_of_admins()
        if message.from_user.id in list(admin_list):
            return True
        else:
            return False
