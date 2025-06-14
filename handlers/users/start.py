from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext

from filters import IsPrivate
from keyboards.default.asosiykeys import main_keys
from keyboards.inline.wikipedia_keys import contact_key

from loader import dp
# from utils.db_api.used_db import add_user, get_user, all_users_count, all_users_list

file_path = "data/myusers"

@dp.message_handler(IsPrivate(), CommandStart())
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username
    user_first_name = message.from_user.first_name
    user_last_name = message.from_user.last_name
    # if get_user(user_id) == None:
    #     add_user(user_id,username,user_first_name,user_last_name)

    # with open(file_path, "r+") as user:
    #     all_user = user.readlines()
    #     if user_id not in all_user:
    #         print(all_user)
    #         user.write(user_id)

    await message.answer(f"Salom, {message.from_user.full_name}!",
                         reply_markup=main_keys)

@dp.message_handler(commands="allusers")
async def all_users(msg:types.Message):
    # all_users = all_users_count()

    # with open(file_path, "r") as user:
    #     all_user = user.readlines()
    #     print(all_user)
    await msg.answer(f"sizning jami foydalnuvchilaringiz soni {all_users} ta")

@dp.message_handler(commands="all")
async def all_users_list2(msg:types.Message):
    # all_users = all_users_list()
    #
    # with open(file_path, "r") as user:
    #     all_user = user.readlines()
    #     print(all_user)
    # await msg.answer(f"sizning jami foydalnuvchilaringiz soni {all_users} ta")
    await msg.answer(f"sizning jami foydalnuvchilaringiz soni ta")


@dp.message_handler(text='🚪 exit', state = ['Tarjima','Wiki'])
async def xolat_exit(message: types.Message, state:FSMContext):
    await message.answer(f"Holatlardan chiqdingiz")
    await state.finish()


@dp.message_handler(text="Bog'lanish")
async def contact_admin(msg: types.Message):
    xabar = f"Adminlar bilan bog'lanish"
    await  msg.answer(xabar, reply_markup=contact_key)
