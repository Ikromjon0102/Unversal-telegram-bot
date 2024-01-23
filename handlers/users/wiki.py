from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
import wikipedia

from keyboards.inline.wikipedia_keys import wikikeys
from loader import dp


@dp.message_handler(text = "Wikipedia")
async def tar_holat(message: types.Message, state:FSMContext):
    await message.answer('siz wiki xolatidasiz, '
                         'wiki qilinishi kerak bolgan malumotni yuboring',
                         reply_markup=wikikeys)

    await state.set_state('Wiki')


@dp.callback_query_handler(text="uzwiki", state = "Wiki")
async def wiki(query: types.CallbackQuery, state: FSMContext):
    await query.message.answer("Message, Siz O'zbek tilini tanladiz, ")
    await query.answer("query, Siz O'zbek tilini tanladiz, ")
    await query.answer(cache_time=60)
    await query.message.delete()

    await state.set_state("uzwikipedia")

@dp.message_handler(state="uzwikipedia")
async def uzwik(msg:types.Message, state: FSMContext):
    wikipedia.set_lang("uz")
    word = msg.text
    natija = wikipedia.summary(word)
    await msg.answer(f"Siz so'ragan maqola\n{natija}")
    await state.finish()
