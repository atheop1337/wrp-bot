from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import CommandStart, Command
from modules.handlers import start_handler, flarum_handler, sender_handler
from modules.libraries.utils import _states
import logging, asyncio

router = Router()


@router.message(CommandStart())
async def start_handler_command(message: types.Message):
    await start_handler.handle_start(message)


@router.callback_query(F.data == "change_flarum")
async def change_flarum_callback(query: types.CallbackQuery, state: FSMContext):
    await flarum_handler.handle_flarum(query, state)


@router.message(_states.ChangeFlarum.new_flarum)
async def change_flarum_state(message: types.Message, state: FSMContext):
    await flarum_handler.handle_flarum(message, state)


@router.callback_query(F.data == "send_message")
async def send_message_callback(query: types.CallbackQuery, state: FSMContext):
    await sender_handler.handle_sender(query, state)


@router.message(_states.SendMessage.dis_id)
async def send_message_id(message: types.Message, state: FSMContext):
    await sender_handler.handle_sender(message, state)


@router.message(_states.SendMessage.message)
async def send_message(message: types.Message, state: FSMContext):
    await sender_handler.handle_sender(message, state)
