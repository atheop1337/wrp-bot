import random, string
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.fsm.state import State, StatesGroup
from modules.libraries.dbms import Database


class const:
    DATABASE_NAME = "database/wrp.db"


class _random_things:

    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_uppercase + string.digits
        return "".join(random.choice(letters) for _ in range(length))


class _kbs:

    @staticmethod
    def get_welcome_kb() -> InlineKeyboardMarkup:
        kb = [
            [
                InlineKeyboardButton(
                    text="📩 Send message", callback_data="send_message"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🎂 Change Flarum", callback_data="change_flarum"
                )
            ],
        ]

        return InlineKeyboardMarkup(inline_keyboard=kb)


class _states:

    class ChangeFlarum(StatesGroup):
        new_flarum = State()

    class SendMessage(StatesGroup):
        dis_id = State()
        message = State()
