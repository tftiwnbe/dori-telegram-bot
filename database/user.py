from aiomysql import Pool
from database.connect import db_connect


class Users:
    pool: Pool = db_connect

    async def id_of_users(self):
        async with self.pool.acquire() as conn:
            async with conn.cursor() as cur:
                sql = "SELECT `user_id` FROM `users`;"
                await cur.execute(sql)
                # Используем списковое включение и распаковку значений
                result = [user_id for (user_id,) in await cur.fetchall()]
                return tuple(result)  # преобразуем список в кортеж

    async def search_user(self, user_id):  # Проверка наличия пользователя в базе данных
        async with self.pool.acquire() as conn:
            async with conn.cursor() as cur:
                sql = "SELECT * FROM users WHERE user_id = %s"
                await cur.execute(sql, user_id)
                return await cur.fetchone()

    async def add_user(self, user):  # Добавление пользователя в базу данных
        async with self.pool.acquire() as conn:
            async with conn.cursor() as cur:
                sql = "INSERT INTO users (user_id, username, first_name, last_name) VALUES (%s, %s, %s, %s)"
                values = (
                    user.id,
                    user.username,
                    user.first_name,
                    user.last_name,
                )
                await cur.execute(sql, values)
                return await cur.fetchone()

    async def all_users_list(self):
        async with self.pool.acquire() as conn:
            async with conn.cursor() as cur:
                sql = "SELECT `user_id` FROM users;"
                await cur.execute(sql)
                users_list = await cur.fetchall()
                return users_list
