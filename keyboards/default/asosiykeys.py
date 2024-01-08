from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


main_keys = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Tarjima"),
            KeyboardButton(text="Wikipedia"),
        ],
        [
            KeyboardButton(text="🚪 exit"),
        ],
        [
            KeyboardButton(text="Bog'lanish", request_contact=True),
            KeyboardButton(text="joylashuvni yuborish", request_location=True),
        ]

    ],
    resize_keyboard=True
)


trans_keys = ReplyKeyboardMarkup(
    keyboard= [
        [
            KeyboardButton(text="English 2 Uzbek"),
            KeyboardButton(text="Uzbek 2 English"),
        ],
        [
            KeyboardButton(text="Russian 2 Uzbek"),
            KeyboardButton(text="Uzbek 2 Russian"),
        ],
        [
            KeyboardButton(text="Russian 2 English"),
            KeyboardButton(text="English 2 Russian"),
        ],
        [
            KeyboardButton(text="Exit")
        ]

    ]











)