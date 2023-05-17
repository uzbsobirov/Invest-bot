from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from data import config


class Database:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME,
        )

    async def execute(
            self,
            command,
            *args,
            fetch: bool = False,
            fetchval: bool = False,
            fetchrow: bool = False,
            execute: bool = False,
    ):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
        id SERIAL PRIMARY KEY,
        full_name VARCHAR(255) NOT NULL,
        username varchar(255) NULL,
        user_id BIGINT NOT NULL UNIQUE,
        crypto TEXT,
        money BigInt,
        input_money BigInt,
        percent TEXT,
        linking TEXT,
        parent_id BigInt,
        count BigInt,
        is_try TEXT,
        date BigInt,
        friend_id BigInt
        );
        """
        await self.execute(sql, execute=True)

    async def create_table_user_lang(self):
        sql = """
        CREATE TABLE IF NOT EXISTS lang_users (
        id SERIAL PRIMARY KEY,
        full_name VARCHAR(255) NOT NULL,
        username varchar(255) NULL,
        user_id BIGINT NOT NULL UNIQUE,
        lang VARCHAR(5)
        );
        """
        await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join(
            [f"{item} = ${num}" for num, item in enumerate(parameters.keys(), start=1)]
        )
        return sql, tuple(parameters.values())

    async def add_user(self, full_name: str, username: str, user_id: int, money: int, linking: str, parent_id: int,
                       count: int, is_try: str):
        sql = "INSERT INTO users (full_name, username, user_id, money, linking, parent_id, count, is_try) VALUES($1, " \
              "$2, $3, $4, $5, $6, $7, $8) returning *"
        return await self.execute(sql, full_name, username, user_id, money, linking, parent_id, count, is_try,
                                  fetchrow=True)

    async def add_user_lang(self, full_name: str, username: str, user_id: int, lang: str):
        sql = "INSERT INTO lang_users (full_name, username, user_id, lang) VALUES($1, $2, $3, $4) returning *"
        return await self.execute(sql, full_name, username, user_id, lang, fetchrow=True)

    async def add_sponsor(self, chat_id: int):
        sql = "INSERT INTO Sponsor (chat_id) VALUES($1) returning *"
        return await self.execute(sql, chat_id, fetchrow=True)

    async def select_all_users(self):
        sql = "SELECT * FROM Users"
        return await self.execute(sql, fetch=True)

    async def select_all_lang(self):
        sql = "SELECT * FROM lang_users"
        return await self.execute(sql, fetch=True)

    async def select_one_user(self, user_id):
        sql = "SELECT * FROM Users WHERE user_id=$1"
        return await self.execute(sql, user_id, fetch=True)

    async def select_user(self, user_id):
        sql = "SELECT * FROM Users WHERE user_id=$1"
        await self.execute(sql, user_id, fetch=True)

    async def select_user_lang(self, user_id):
        sql = "SELECT * FROM lang_users WHERE user_id=$1"
        return await self.execute(sql, user_id, fetch=True)

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM Users"
        return await self.execute(sql, fetchval=True)

    async def update_user_count(self, user_id):
        sql = "UPDATE Users SET count=count+1 WHERE user_id=$1"
        return await self.execute(sql, user_id, execute=True)

    async def update_user_money(self, money, user_id):
        sql = "SELECT money FROM Users WHERE user_id=$1"
        result = await self.execute(sql, user_id, fetch=True)
        if result:
            money = result[0][0] + money
        sql = "UPDATE Users SET money=$1 WHERE user_id=$2"
        return await self.execute(sql, money, user_id, execute=True)

    async def get_lang(self, user_id):
        sql = "SELECT lang FROM lang_users WHERE user_id=$1"
        return await self.execute(sql, user_id, fetch=True)

    async def update_user_new_money(self, money, user_id):
        sql = "UPDATE Users SET money=$1 WHERE user_id=$2"
        return await self.execute(sql, money, user_id, execute=True)

    async def update_user_language(self, lang, user_id):
        sql = "UPDATE lang_users SET lang=$1 WHERE user_id=$2"
        return await self.execute(sql, lang, user_id, execute=True)

    async def update_user_date(self, user_id):
        sql = "UPDATE Users SET date=date-1 WHERE user_id=$1"
        return await self.execute(sql, user_id, execute=True)

    async def update_user_money_pay(self, money, crypto, date, user_id):
        sql = "UPDATE Users SET money=$1, crypto=$2, date=$3 WHERE user_id=$4"
        return await self.execute(sql, money, crypto, date, user_id, execute=True)

    async def update_user_is_try(self, is_try, user_id):
        sql = "UPDATE Users SET is_try=$1 WHERE user_id=$2"
        return await self.execute(sql, is_try, user_id, execute=True)

    async def drop_courses(self):
        await self.execute("DROP TABLE Courses", execute=True)
