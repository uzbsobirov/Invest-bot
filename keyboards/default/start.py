from aiogram.types import KeyboardButton, ReplyKeyboardMarkup



start = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="✳️ Vip tariflar"
            ),
            KeyboardButton(
                text="💰 Balans"
            )
        ],
        [
            KeyboardButton(
                text="🆘 Murojaat uchun admin_panel"
            )
        ],
        [
            KeyboardButton(
                text="🔗 Referal"
            ),
            KeyboardButton(
                text="📰 Bot haqida"
            )
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)

start_admin = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="✳️ Vip tariflar"
            ),
            KeyboardButton(
                text="💰 Balans"
            )
        ],
        [
            KeyboardButton(
                text="🆘 Murojaat uchun admin_panel"
            )
        ],
        [
            KeyboardButton(
                text="🔗 Referal"
            ),
            KeyboardButton(
                text="📰 Bot haqida"
            )
        ],
        [
            KeyboardButton(
                text="💻 Admin panel"
            )
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)