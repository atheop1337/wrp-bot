from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.enums import ChatAction
from modules.libraries.dbms import Database
from modules.libraries.utils import _kbs, _states, const
from modules.libraries.sender import Sender
import asyncio


class StartHandler:

    def __init__(self, db: str):
        self.db = Database(db)

    async def handle_start(self, message: types.Message):

        userID = message.from_user.id
        userNAME = message.from_user.username

        await self.db.add_user(userID, userNAME)

        await message.answer(
            "Привет! Это блабалаблабалабаллабаб", reply_markup=_kbs.get_welcome_kb()
        )


class FlarumHandler:

    def __init__(self, db: str):
        self.db = Database(db)

    async def handle_flarum(self, _type, state: FSMContext):

        if isinstance(_type, types.CallbackQuery):
            await _type.message.answer("Новое значение фларума")
            await state.set_state(_states.ChangeFlarum.new_flarum)

        elif isinstance(_type, types.Message):
            userID = _type.from_user.id

            if await self.db.edit_info(userID, "flarum", _type.text):
                await _type.answer(f"Flarum изменен на {_type.text}")
            else:
                await _type.answer("Ошибка при изменении Flarum")

            await state.clear()


class SenderHandler:

    def __init__(self, db: str):
        self.db = Database(db)

    async def handle_sender(self, _type, state: FSMContext):

        if isinstance(_type, types.CallbackQuery):

            userID = _type.from_user.id

            data = await self.db.fetch_info("userID", userID)
            flarum = data.get("flarum")
            if flarum == "NULL":
                await _type.answer("Фларум == нулл", show_alert=True)
                return

            await _type.message.answer("Введите айди дискуссии")
            await state.set_state(_states.SendMessage.dis_id)

        elif isinstance(_type, types.Message):
            current_state = await state.get_state()

            if current_state == _states.SendMessage.dis_id:
                try:
                    int(_type.text)
                except ValueError:
                    await _type.answer("Айди дискуссии должно быть числом")
                    return

                await state.update_data(dis_id=_type.text)
                await _type.answer("Введите текст сообщения")
                await state.set_state(_states.SendMessage.message)

            elif current_state == _states.SendMessage.message:
                data = await state.get_data()
                dis_id = data.get("dis_id")
                _message = _type.text

                await _type.bot.send_chat_action(
                    chat_id=_type.chat.id, action=ChatAction.TYPING
                )

                sender = Sender(
                    const.DATABASE_NAME, dis_id, _message, _type.from_user.id
                )

                answer = await sender.send_message()

                await _type.answer(answer)

                await state.clear()
