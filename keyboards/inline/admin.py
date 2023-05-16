from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from language import i18n

_ = i18n.gettext


admin = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text=_("📊 Statistika"), callback_data='statistic'
            ),
            InlineKeyboardButton(
                text=_("🗞 Xabar yuborish"), callback_data='send_message'
            )
        ],
        [
            InlineKeyboardButton(
                text=_("➕ Pul kiritish"), callback_data='pay_to_user'
            )
        ],
        [
            InlineKeyboardButton(
                text=_("◀️ Orqaga"), callback_data='back'
            )
        ]
    ]
)

cryptos = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text=_("Premium BTC"), callback_data='premiumbtc'
            ),
            InlineKeyboardButton(
                text=_("Standart ETH"), callback_data='standarteth'
            ),
            InlineKeyboardButton(
                text=_("Maximum LTC"), callback_data='maximumltc'
            )
        ],
        [
            InlineKeyboardButton(
                text=_("◀️ Orqaga"), callback_data='back'
            )
        ]
    ]
)
