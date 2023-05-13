from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



langs = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🇺🇿 O'zbek", callback_data='uz'
            )
        ],
        [
            InlineKeyboardButton(
                text="🇷🇺 Русский", callback_data='ru'
            )
        ]
    ]
)