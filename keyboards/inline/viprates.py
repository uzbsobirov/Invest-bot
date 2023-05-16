from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from language import i18n

_ = i18n.gettext

rates = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text=_("Premium BTC"), callback_data='premiumbtc'
            )
        ],
        [
            InlineKeyboardButton(
                text=_("Standart ETH"), callback_data='standarteth'
            )
        ],
        [
            InlineKeyboardButton(
                text=_("Maximum LTC"), callback_data='maximumltc'
            )
        ],
        [
            InlineKeyboardButton(
                text=_("◀️ Orqaga"), callback_data='back_to_main'
            )
        ]
    ]
)