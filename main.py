"""
AUTHOR: github.com/atheop1337 😘
"""

import asyncio, logging, os
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from modules.routers import router as handlers_router
from aiogram.enums import ParseMode
from modules.libraries.dbms import Database
from datetime import datetime
from modules.libraries.utils import const


TOKEN_FILE_PATH = "tokens\\TOKEN"


def read_token_from_file(file_path) -> str:
    try:
        with open(file_path, "r") as file:
            token = file.read().strip()
            return token
    except Exception as e:
        raise ValueError(f"Error reading token from file: {e}")


TOKEN = read_token_from_file(TOKEN_FILE_PATH)
if not TOKEN:
    raise ValueError("No BOT_TOKEN found in the token file. Please check your token.")


async def main() -> None:
    db = Database(const.DATABASE_NAME)
    await db.connect()
    dp = Dispatcher()
    dp.include_routers(handlers_router)
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
        await db.close()


if __name__ == "__main__":
    try:
        logging.basicConfig(
            level=logging.INFO,
            format="[%(asctime)s]:%(levelname)s:%(funcName)s:%(message)s",
            datefmt="%Y-%m-%d|%H:%M:%S",
        )
        logging.info(f"Using {'WIN' if os.name == 'nt' else 'UNIX'} base kernel")
        asyncio.run(main())
    except Exception as e:
        print(f"An error occurred: {e}")
        logging.exception("An error occurred")
