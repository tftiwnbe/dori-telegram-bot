from aiomysql import Pool
from database.connect import db_connect


class Admin:
    pool: Pool = db_connect

    async def list_of_admins(self):
        async with self.pool.acquire() as conn:
            async with conn.cursor() as cur:
                sql = "SELECT `user_id` FROM `users` WHERE `admin` = 1;"
                await cur.execute(sql)
                # Используем списковое включение и распаковку значений
                result = [user_id for (user_id,) in await cur.fetchall()]
                return tuple(result)  # преобразуем список в кортеж

    async def list_of_all_users(self):  # Выводим список всех пользоавтелей
        async with self.pool.acquire() as conn:
            async with conn.cursor() as cur:
                sql = "SELECT `id`, `user_id`, `username`, `first_name`, `last_name` FROM `users`;"
                await cur.execute(sql)
                users = await cur.fetchall()
                columns = [
                    desc[0] for desc in cur.description
                ]  # получаем описание столбцов
                users_list = [
                    dict(zip(columns, user)) for user in users
                ]  # создает пары ключ-значение для каждого кортежа

                return users_list  # в конечном итоге получаем словарь для каждого пользователя

    async def count_users(self):  # считаем пользователей
        async with self.pool.acquire() as conn:
            async with conn.cursor() as cur:
                # Запрос для количества всех пользователей
                sql_total_users = "SELECT COUNT(`id`) as `total_users` FROM users;"
                await cur.execute(sql_total_users)
                total_users_count = await cur.fetchone()

                # Запрос для количества администраторов
                sql_admin_users = "SELECT COUNT(`admin`) as `admin_users` FROM users WHERE `admin` = 1;"
                await cur.execute(sql_admin_users)
                admin_users_count = await cur.fetchone()

                # Запрос для количества пользователей подписавшихся на расписание
                sql_subscribed_users = "SELECT COUNT(`subscribe_time`) as `subscribed_users` FROM users WHERE `subscribe_time` = 1;"
                await cur.execute(sql_subscribed_users)
                subscribed_users_count = await cur.fetchone()

                # Возвращаем результат в виде словаря
                return {
                    "total_users": total_users_count[0],
                    "admin_users": admin_users_count[0],
                    "subscribed_users": subscribed_users_count[0],
                }
