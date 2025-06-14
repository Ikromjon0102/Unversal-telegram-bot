from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from keyboards.default.asosiykeys import main_keys
from keyboards.inline.wikipedia_keys import contact_key

from loader import dp
file_path = "data/myusers"

@dp.message_handler(commands="html")
async def bot_start(message: types.Message):
    text = "Bu qalinmas matn\n"
    text += "<b>Bu qalin matn</b>    \n"
    text += "<i> Bu qiyshiq matn </i>    \n"
    text += "<u>underline1</u>, <ins>underline2</ins>    \n"
    text += "<s>xatolik</s>    \n"
    text += "<span class='tg-spoiler'>yashirin matn</span>    \n"
    text += "<tg-spoiler>yashirin matn</tg-spoiler>    \n"
    text += "<b> <i> qiyshiq semiz matn </i> </b>    \n"
    text += "<b> <i> <tg-spoiler> qiyshiq semiz matn </tg-spoiler> </i> </b>    \n"
    # text += "<a href='https://www.youtube.com/'>youtube</a>    \n"
#     text += """<code> executor.py [LINE:362] #INFO     [2024-02-08 16:40:18,654]  Bot: Sariq Dev [@saariqdevbot]
# dispatcher.py [LINE:359] #INFO     [2024-02-08 16:40:18,980]  Start polling. </code>    \n"""
#
#     text += """
#     ```
#     @dp.message_handler(CommandStart())
# async def bot_start(message: types.Message):
#     user_id = str(message.from_user.id) + "\n"
#     with open(file_path, "r+") as user:
#         all_user = user.readlines()
#         if user_id not in all_user:
#             print(all_user)
#             user.write(user_id)
#
#
#     await message.answer(f"Salom, {message.from_user.full_name}!",
#                          reply_markup=main_keys)
#     ```
#     """

    # text += """<pre> @dp.message_handler(CommandStart())
    #     async def bot_start(message: types.Message):
    #         user_id = str(message.from_user.id) + "\n"
    #         with open(file_path, "r+") as user:
    #             all_user = user.readlines()
    #             if user_id not in all_user:
    #                 print(all_user)
    #                 user.write(user_id)
    #
    #
    #         await message.answer(f"Salom, {message.from_user.full_name}!",
    #                              reply_markup=main_keys) </pre>    \n"""

    text += "<blockquote>Block quotation started\nBlock quotation continued\nThe last line of the block quotation</blockquote>"

    await message.answer(text)


@dp.message_handler(commands="mark")
async def bot_start(message: types.Message):
    text = "* bold \*text* \n"
    text += "_ italic \*text_ \n"
    text += "__ underline \*text__ \n"
    text += "~ strike \*text~ \n"
    text += "|| spolier \*text || \n"
    text += "> quota \*text  \n"
    text += "__ salom_alik __  \n"

    await message.answer(text)