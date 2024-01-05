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