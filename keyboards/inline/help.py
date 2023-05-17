from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from language import i18n

_ = i18n.lazy_gettext

help = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text=_("🆘 Admin"), url='t.me/kayzenuz'
            )
        ]
    ]
)