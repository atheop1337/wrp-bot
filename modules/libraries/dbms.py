import aiosqlite
import asyncio
import logging


class Database:
    def __init__(self, const):
        self.db_path = const

    async def connect(self):
        self.conn = await aiosqlite.connect(self.db_path)
        await self.create_tables()

    async def create_tables(self):
        async with aiosqlite.connect(self.db_path) as db:
            async with db.cursor() as cursor:
                await cursor.execute(
                    """
                    CREATE TABLE IF NOT EXISTS user_data (
                        id INTEGER PRIMARY KEY,
                        userID INTEGER UNIQUE,
                        userNAME TEXT NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        flarum TEXT DEFAULT NULL
                    )
                    """
                )
                await db.commit()

    async def add_user(self, userID: int, userNAME: str) -> None:
        try:
            async with aiosqlite.connect(self.db_path) as db:
                async with db.cursor() as cursor:
                    await cursor.execute(
                        """
                        INSERT INTO user_data (userID, userNAME)
                        VALUES (?,?)
                        """,
                        (userID, userNAME),
                    )
                    await db.commit()
        except aiosqlite.IntegrityError:
            pass
        except aiosqlite.Error as e:
            logging.exception(f"Exception | add_user func: {e}")

    async def fetch_info(self, identifier: str, value: any) -> dict:
        try:
            async with aiosqlite.connect(self.db_path) as db:
                async with db.cursor() as cursor:
                    await cursor.execute(
                        f"""
                        SELECT * FROM user_data
                        WHERE {identifier}=?
                        """,
                        (value,),
                    )
                    row = await cursor.fetchone()
                    return {
                        "id": row[0],
                        "userID": row[1],
                        "userNAME": row[2],
                        "created_at": row[3],
                        "flarum": row[4],
                    }
        except aiosqlite.Error as e:
            logging.exception(f"Exception | fetch_info func: {e}")
            return {}

    async def edit_info(self, user_id: int, identifier: str, value: any) -> None:
        try:
            async with aiosqlite.connect(self.db_path) as db:
                async with db.cursor() as cursor:
                    await cursor.execute(
                        f"""
                        UPDATE user_data
                        SET {identifier}=?
                        WHERE userID=?
                        """,
                        (value, user_id),
                    )
                    await db.commit()
                    return True
        except aiosqlite.Error as e:
            logging.exception(f"Exception | edit_info func: {e}")
            return False

    async def close(self) -> None:
        if self.conn:
            await self.conn.close()
