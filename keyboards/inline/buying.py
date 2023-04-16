from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

buying = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="📨 Bog'lanish", url='https://t.me/Rasul_Maxmudov'
            )
        ],
        [
            InlineKeyboardButton(
                text="◀️ Orqaga", callback_data='back_to_cards'
            )
        ]
    ]
)