from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
import wikipedia

from loader import dp


@dp.message_handler(commands=['wiki'])
async def tar_holat(message: types.Message, state:FSMContext):
    await message.answer('siz wiki xolatidasiz, '
                         'wiki qilinishi kerak bolgan malumotni yuboring')
    await state.set_state('Wiki')


@dp.message_handler(state='Wiki')
async def wiki(message: types.Message):
    text = message.text
    wiki_natija = wikipedia.summary(text)

    await message.answer(f"NATIJA, {wiki_natija}")
