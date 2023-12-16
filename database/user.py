from aiomysql import Pool
from database.connect import db_connect


class Users:
    pool: Pool = db_connect

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
