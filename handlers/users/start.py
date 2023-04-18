from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.utils.deep_linking import get_start_link

from keyboards.default.start import start
from loader import dp, db, bot


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message):
    full_name = message.from_user.full_name
    username = message.from_user.username
    user_id = message.from_user.id
    user_mention = message.from_user.get_mention(name=full_name, as_html=True)
    linking = await get_start_link(user_id)
    parent_id = message.get_args()

    # Add the User to the DB
    try:
        if parent_id:
            await db.add_user(
                full_name=full_name,
                username=username,
                user_id=user_id,
                money=0,
                linking=linking,
                parent_id=parent_id,
                count=0
            )
        else:
            await db.add_user(
                full_name=full_name,
                username=username,
                user_id=user_id,
                money=0,
                linking=linking,
                parent_id=7,
                count=0
            )

    except:
        pass

    start_text = "<b>Assalomu aleykum hurmatli mijoz! Siz bu bot orqali kriptovalyutalarga investitsiya " \
                 "kiritib olishingiz mumkin</b>"
    await message.answer(text=start_text, reply_markup=start)
