from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from language import i18n

_ = i18n.lazy_gettext


withdraw = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text=_("📤 Pul chiqarish"), callback_data='withdrawmoney'
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