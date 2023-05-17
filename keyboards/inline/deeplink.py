from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from language import i18n

_ = i18n.lazy_gettext

def deep_link_share(user_id, bot_username):
    markup = InlineKeyboardMarkup()
    markup.insert(
        InlineKeyboardButton(
            text=_("📲 Do'stlarga ulashish"),
            switch_inline_query=f'https://t.me/{bot_username}?start={user_id} -- ga kirib pul ishlang'
        )
    )
    return markup