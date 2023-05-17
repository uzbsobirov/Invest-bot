from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from language import i18n

_ = i18n.lazy_gettext

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
            ),
            InlineKeyboardButton(
                text="🔸 Binance", callback_data='binance'
            )
        ],
        [
            InlineKeyboardButton(
                text=_("◀️ Orqaga"), callback_data='back_to_rates'
            )
        ]
    ]
)