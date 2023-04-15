from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

back_rates = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="✅ Sotib olish", callback_data='buy'
            )
        ],
        [
            InlineKeyboardButton(
                text="◀️ Orqaga", callback_data='back'
            )
        ]
    ]
)