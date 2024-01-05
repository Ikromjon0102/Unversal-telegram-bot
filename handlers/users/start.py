from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from keyboards.default.asosiykeys import main_keys

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",
                         reply_markup=main_keys)

@dp.message_handler(text='🚪 exit', state = ['Tarjima','Wiki'])
async def xolat_exit(message: types.Message, state:FSMContext):
    await message.answer(f"Holatlardan chiqdingiz")
    await state.finish()


