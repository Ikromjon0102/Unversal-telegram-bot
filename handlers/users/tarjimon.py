from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from keyboards.default.asosiykeys import trans_keys,main_keys
from aiogram.types import ReplyKeyboardRemove

from googletrans import Translator

tarjima = Translator()

from loader import dp

@dp.message_handler(text="Tarjima")
async def tar_holat(message: types.Message, state:FSMContext):
    await message.answer('siz tarjimon xolatidasiz, '
                         'tarjima qilinishi kerak bolgan tilni tanlang',
                         reply_markup=trans_keys)
    await state.set_state('Tarjima')


@dp.message_handler(text = "English 2 Uzbek", state=['Tarjima', "eng2uz"])
async def tarjima_en2uz(message: types.Message, state:FSMContext):
    await message.answer(f"English 2 Uzbek\n matn yuboring",
                         reply_markup=ReplyKeyboardRemove())
    await state.set_state("eng2uz")

@dp.message_handler(state='eng2uz')
async def tar_en2uz(message: types.Message, state:FSMContext):
    text = message.text
    tar = tarjima.translate(text, "uz").text
    await message.answer(f"Tarjima natijasi\n{tar}",
                         reply_markup=trans_keys)
    await state.set_state("Tarjima")

@dp.message_handler(text = "Uzbek 2 English", state=['Tarjima',"eng2uz", "uz2eng"])
async def tarjima_uz2en(message: types.Message, state:FSMContext):
    await message.answer(f"Uzbek 2 English\n matn yuboring",
                         reply_markup=ReplyKeyboardRemove())
    await state.set_state("uz2eng")

@dp.message_handler(state='uz2eng')
async def tar_uz2en(message: types.Message, state:FSMContext):
    text = message.text
    tar = tarjima.translate(text).text
    await message.answer(f"Tarjima natijasi\n{tar}",
                         reply_markup=main_keys)

    await state.finish()


