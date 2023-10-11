import asyncpg
from configurations.conf import Config


class AsyncDatabase:
    def __init__(self):
        self.config = Config()
        self.dsn = f"postgresql://{self.config.user}:{self.config.password}@{self.config.host}:5432/{self.config.dbase}"

    async def create_pool(self):
        return await asyncpg.create_pool(dsn=self.dsn)

    @staticmethod
    async def execute(pool, sql: str, parameters: tuple = None, fetchone=False, fetchall=False):
        if not parameters:
            parameters = tuple()

        async with pool.acquire() as connection:
            data = None
            async with connection.transaction():
                if fetchone:
                    data = await connection.fetchrow(sql, *parameters)
                elif fetchall:
                    data = await connection.fetch(sql, *parameters)
                else:
                    await connection.execute(sql, *parameters)
        return data

    async def select_tokens(self, pool):
        sql = '''
            SELECT id, "tokenAccess", "tokenRefresh" FROM tokens WHERE id = 1
        '''
        return await self.execute(pool, sql, fetchone=True)
