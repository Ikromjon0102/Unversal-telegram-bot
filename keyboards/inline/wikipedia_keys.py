from aiogram.types import (InlineKeyboardMarkup,
                           InlineKeyboardButton)

from .calback_data import book_callback

# 1-usuli,
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

# 2 - usul

contact_key = InlineKeyboardMarkup(row_width=1)

admin = InlineKeyboardButton(text="Admin", callback_data="admin")
y_admin = InlineKeyboardButton(text="II admin", url="https://t.me/ikromjon_ergashev")
contact_key.add(admin)
contact_key.add(y_admin)
ykey = InlineKeyboardButton(text="YouTube", url="https://www.youtube.com/watch?v=TnuPn_rcH_E")
contact_key.add(ykey)


# 3 - usul
books = {
    "Python asoslari": "python",
    "Welcome to Java for Python Programmers": "java",
    "A Complete Guide to Standard C++ Algorithms": "c++",
    "Basic JavaScript for the impatient programmer": "js"
}

book_keys = InlineKeyboardMarkup(row_width=1)

for key, value in books.items():
    book_keys.insert(InlineKeyboardButton(text=key, callback_data=book_callback.new(item_name = value)))

book_keys.insert(ykey)

















