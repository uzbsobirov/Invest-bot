from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def deep_link_share(user_id, bot_username):
    markup = InlineKeyboardMarkup()
    markup.insert(
        InlineKeyboardButton(
            text="📲 Do'stlarga ulashish",
            switch_inline_query=f'https://t.me/{bot_username}?start={user_id} -- ga kirib pul ishlang'
        )
    )
    return markup