from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



buying = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="📨 Bog'lanish", url='https://t.me/Rasul_Maxmudov'
            )
        ],
        [
            InlineKeyboardButton(
                text="◀️ Orqaga", callback_data='back_to_cards'
            )
        ]
    ]
)


# def payload(user_id, crypto):
#     markup = InlineKeyboardMarkup(row_width=1)
#     markup.insert(
#         InlineKeyboardButton(
#             text="✅ To'lash", callback_data=f'tolandi_{user_id}_{crypto}'
#         )
#     )
#     markup.insert(
#         InlineKeyboardButton(
#             text="❌ Bekor qilish", callback_data=f'bekor_tolov_{user_id}_{crypto}'
#         )
#     )
#     return markup

payload = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="✅ To'lash", callback_data='accept_payload'
            )
        ],
        [
            InlineKeyboardButton(
                text="❌ Bekor qilish", callback_data='cancel_payload'
            )
        ]
    ]
)