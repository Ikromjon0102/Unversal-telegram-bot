from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp
from filters.groupfilter import IsGroup
from filters.adminfilter import IsAdmin

@dp.message_handler(IsGroup(), CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}! siz guruhdasiz")


