from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from language import i18n

_ = i18n.gettext()

start = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text=_("✳️ Vip tariflar")
            )
        ],
        [
            KeyboardButton(
                text=_("☎️ Murojaat uchun")
            ),
            KeyboardButton(
                text=_("💰 Balans")
            )
        ],
        [
            KeyboardButton(
                text=_("🔗 Referal")
            ),
            KeyboardButton(
                text=_("📰 Bot haqida")
            )
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)

start_admin = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text=_("✳️ Vip tariflar")
            )
        ],
        [
            KeyboardButton(
                text=_("☎️ Murojaat uchun")
            ),
            KeyboardButton(
                text=_("💰 Balans")
            )
        ],
        [
            KeyboardButton(
                text=_("🔗 Referal")
            ),
            KeyboardButton(
                text=_("📰 Bot haqida")
            )
        ],
        [
            KeyboardButton(
                text=_("💻 Admin panel")
            )
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)