
import re
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, Text
from aiogram.dispatcher.filters import Regexp
from loader import dp
from filters.groupfilter import IsGroup


@dp.message_handler(IsGroup(), content_types=types.ContentTypes.NEW_CHAT_MEMBERS)
async def new_chat_member(message: types.Message):
    await message.delete()
    # print(message)
    await message.answer(f"hush kelibsiz, {message.new_chat_members[0].full_name}! Hush kelibsiz")

@dp.message_handler(IsGroup(), content_types=types.ContentTypes.LEFT_CHAT_MEMBER)
async def left_chat_member(message: types.Message):
    await message.delete()
    # print(message.left_chat_member.full_name)
    await message.answer(f"foydalanuvchi {message.left_chat_member.full_name}! guruxni tark etdi")

# @dp.message_handler(IsGroup(), Text(contains="http"))
# async def delete_link(message: types.Message):
#     await message.delete()
#     print(message.text)
#     await message.answer(f"Hurmatli {message.from_user.first_name}! link yuborish taqiqlanadi")
# #
# @dp.message_handler(IsGroup(), Regexp(URL_REGEX))
# async def delete_link2(message: types.Message):
#     # await message.delete()
#     print(message)
#     await message.answer(f"Hurmatli {message.from_user.first_name}! url  yuborish taqiqlanadi")
# #


@dp.message_handler(IsGroup())
async def unban_user(message: types.Message):
    url_extract_pattern = "https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)"
    rek = re.findall(url_extract_pattern, message.text)
    words = message.text.split()
    nik = 0
    sokindi = 0
    sozlar = ['jinnimisan','axmoqmisan']
    for i in words:
        if i[0] == "@":
            nik = 1
        if i.lower() in sozlar:
            sokindi = 1
    try:
        if rek or nik:
            await message.answer(f"Hurmatli {message.from_user.full_name} o'zing shunaqasan")
            await message.delete()
        if sokindi:
            await message.answer(f"Hurmatli {message.from_user.full_name} xaqoratli so'zlar ishlatmang!")
            await message.delete()
        if message.entities[0].type == "text_link":
            await message.answer(f"Hurmatli {message.from_user.full_name} reklama tarqatmang!")
            await message.delete()
    except:
        pass
