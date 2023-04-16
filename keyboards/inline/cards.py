from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

cards = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🅿️ Payeer", callback_data='payeer'
            ),
            InlineKeyboardButton(
                text="🐤 Qiwi", callback_data='qiwi'
            )
        ],
        [
            InlineKeyboardButton(
                text="🔹 Payme", callback_data='payme'
            )
        ],
        [
            InlineKeyboardButton(
                text="◀️ Orqaga", callback_data='back_to_rates'
            )
        ]
    ]
)