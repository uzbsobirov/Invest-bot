from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


withdraw = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="📤 Pul chiqarish", callback_data='withdrawmoney'
            )
        ]
    ]
)

payment = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="✅ To'landi", callback_data='successpay'
            )
        ],
        [
            InlineKeyboardButton(
                text="❌ To'lanmadi", callback_data='unsuccesspay'
            )
        ]
    ]
)