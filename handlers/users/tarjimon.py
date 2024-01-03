from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext

from googletrans import Translator

tarjima = Translator()

from loader import dp

@dp.message_handler(commands=['translate'])
async def tar_holat(message: types.Message, state:FSMContext):
    await message.answer('siz tarjimon xolatidasiz, '
                         'tarjima qilinishi kerak bolgan malumotni yuboring')
    await state.set_state('Tarjima')


@dp.message_handler(state='Tarjima')
async def tarji(message: types.Message, state:FSMContext):
    text = message.text
    tarjima_natijasi = tarjima.translate(text=text, dest='uz').text

    await message.answer(f"NATIJA, {tarjima_natijasi}")
    await state.finish()
