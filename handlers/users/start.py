from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.start import start
from loader import dp, db, bot


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message):
    full_name = message.from_user.full_name
    username = message.from_user.username
    user_id = message.from_user.id
    user_mention = message.from_user.get_mention(name=full_name, as_html=True)

    # Add the User to the DB
    try:
        await db.add_user(
            full_name=full_name,
            username=username,
            user_id=user_id,
            money=0
        )

    except:
        pass

    start_text = "<b>Assalomu aleykum hurmatli mijoz! Siz bu bot orqali kriptovalyutalarga investitsiya " \
                 "kiritib olishingiz mumkin</b>"
    await message.answer(text=start_text, reply_markup=start)
