from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from keyboards.default.asosiykeys import main_keys

from loader import dp
file_path = "data/myusers"

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user_id = str(message.from_user.id) + "\n"
    with open(file_path, "r+") as user:
        all_user = user.readlines()
        if user_id not in all_user:
            print(all_user)
            user.write(user_id)


    await message.answer(f"Salom, {message.from_user.full_name}!",
                         reply_markup=main_keys)

@dp.message_handler(commands="allusers")
async def all_users(msg:types.Message):
    with open(file_path, "r") as user:
        all_user = user.readlines()
        print(all_user)
    await msg.answer(f"sizning jami foydalnuvchilaringiz soni {len(all_user)} ta")


@dp.message_handler(text='🚪 exit', state = ['Tarjima','Wiki'])
async def xolat_exit(message: types.Message, state:FSMContext):
    await message.answer(f"Holatlardan chiqdingiz")
    await state.finish()


