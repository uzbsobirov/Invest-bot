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

payload = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="✅ To'lash", callback_data='tolash'
            )
        ],
        [
            InlineKeyboardButton(
                text="❌ Bekor qilish", callback_data='bekor_tolov'
            )
        ]
    ]
)
