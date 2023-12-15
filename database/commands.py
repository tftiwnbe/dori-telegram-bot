from aiomysql import Pool, DictCursor
from .connect import db_connect


class Commands:  # Стандартные команды MySQL
    pool: Pool = db_connect

    async def insert(self, sql, data):
        async with self.pool.acquire() as conn:
            async with conn.cursor(DictCursor) as cur:
                await cur.execute(sql, data)

    async def select_all(self, sql, data):
        async with self.pool.acquire() as conn:
            async with conn.cursor(DictCursor) as cur:
                await cur.execute(sql, data)
                return await cur.fetchall()

    async def select_one(self, sql, data):
        async with self.pool.acquire() as conn:
            async with conn.cursor(DictCursor) as cur:
                await cur.execute(sql, data)
                return await cur.fetchone()
