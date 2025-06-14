from aiogram import types

from keyboards.inline.wikipedia_keys import book_keys
from loader import dp
from keyboards.inline.calback_data import book_callback


@dp.message_handler(text="Kitoblar")
async def kitobhanler(msg: types.Message):
    xabar = "Kitoblardan birini tanlang"
    await msg.answer(xabar, reply_markup=book_keys)


@dp.callback_query_handler(book_callback.filter())
async def pyhandler(call: types.CallbackQuery):
    xabar = ("Siz Pythonda dasturlash asoslari (Anvar Narzullayev) kitobini tanladingiz\n"
             "https://asaxiy.uz/uz/product/anvar-narzullaev-pythonda-dasturlash-asoslari")

    await call.message.answer(xabar)






