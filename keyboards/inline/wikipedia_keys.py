from aiogram.types import (InlineKeyboardMarkup,
                           InlineKeyboardButton)

wikikeys = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="O'zbek wiki", callback_data='uzwiki') ,
            InlineKeyboardButton(text="English wiki", callback_data="enwiki"),
        ],
        [
            InlineKeyboardButton(text="Ruscha wiki", callback_data="ruswiki")
        ]
    ]
)