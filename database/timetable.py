from aiomysql import Pool
from database.connect import db_connect


class Timetable:
    pool: Pool = db_connect

    async def id_of_subscribers(self):
        async with self.pool.acquire() as conn:
            async with conn.cursor() as cur:
                sql = "SELECT `user_id` FROM `users` WHERE `timetable` = 1;"
                await cur.execute(sql)
                # Используем списковое включение и распаковку значений
                result = [user_id for (user_id,) in await cur.fetchall()]
                return tuple(result)  # преобразуем список в кортеж

    # Подписан ли пользователь на расписаниеы
    async def subscribed_user(self, user_id):
        async with self.pool.acquire() as conn:
            async with conn.cursor() as cur:
                sql = f"SELECT `timetable`  FROM `users` WHERE `user_id` = {user_id}"
                await cur.execute(sql)
                status = await cur.fetchone()
                return status[0]

    # Изменить подписку пользователя
    async def toggle_user(self, user_id, toggle: int = 1):
        async with self.pool.acquire() as conn:
            async with conn.cursor() as cur:
                sql = f"UPDATE `users`  SET `timetable` = {toggle} WHERE `user_id` = {user_id};"
                return await cur.execute(sql)
