from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



rates = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Premium BTC", callback_data='premiumbtc'
            ),
            InlineKeyboardButton(
                text="Standart ETH", callback_data='standarteth'
            ),
            InlineKeyboardButton(
                text="Maximum LTC", callback_data='maximumltc'
            )
        ],
        [
            InlineKeyboardButton(
                text="◀️ Orqaga", callback_data='back_to_main'
            )
        ]
    ]
)