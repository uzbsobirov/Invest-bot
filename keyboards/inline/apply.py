from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from language import i18n

_ = i18n.gettext

apply = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text=_("☎️ Metago Admin"), url='https://t.me/metagobot_admin'
            )
        ]
    ]
)