from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



admin = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="📊 Statistika", callback_data='statistic'
            ),
            InlineKeyboardButton(
                text="🗞 Xabar yuborish", callback_data='send_message'
            )
        ],
        [
            InlineKeyboardButton(
                text="📢 Majburiy obuna", callback_data='subscription'
            ),
            InlineKeyboardButton(
                text="➕ Pul kiritish", callback_data='pay_to_user'
            )
        ],
        [
            InlineKeyboardButton(
                text="◀️ Orqaga", callback_data='back'
            )
        ]
    ]
)

cryptos = InlineKeyboardMarkup(
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
                text="◀️ Orqaga", callback_data='back'
            )
        ]
    ]
)


channels_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🗑 Kanalni o'chirish", callback_data='channel_delete'
            ),
            InlineKeyboardButton(
                text="➕ Kanal qo'shish", callback_data='add_channel'
            )
        ],
        [
            InlineKeyboardButton(
                text="◀️ Orqaga", callback_data='back_to_admin_menu'
            )
        ]
    ]
)

channels_menuu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="➕ Kanal qo'shish", callback_data='add_channel'
            )
        ],
        [
            InlineKeyboardButton(
                text="◀️ Orqaga", callback_data='back_to_admin_menu'
            )
        ]
    ]
)