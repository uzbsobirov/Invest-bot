from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from language import i18n

_ = i18n.gettext


back_btc = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text=_("✅ Sotib olish"), callback_data='buy_btc'
            )
        ],
        [
            InlineKeyboardButton(
                text=_("◀️ Orqaga"), callback_data='back'
            )
        ]
    ]
)

back_eth = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text=_("✅ Sotib olish"), callback_data='buy_eth'
            )
        ],
        [
            InlineKeyboardButton(
                text=_("◀️ Orqaga"), callback_data='back'
            )
        ]
    ]
)

back_ltc = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text=_("✅ Sotib olish"), callback_data='buy_ltc'
            )
        ],
        [
            InlineKeyboardButton(
                text=_("◀️ Orqaga"), callback_data='back'
            )
        ]
    ]
)


back = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text=_("◀️ Orqaga"), callback_data='back'
            )
        ]
    ]
)

back_sponsor = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text=_("◀️ Orqaga"), callback_data='back_sponsor'
            )
        ]
    ]
)