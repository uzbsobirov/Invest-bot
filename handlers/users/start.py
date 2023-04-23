import logging

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.utils.deep_linking import get_start_link

from data.config import ADMINS
from keyboards.default.start import start, start_admin
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
                parent_id=int(parent_id),
                count=0,
                is_try='yes'
            )
        else:
            await db.add_user(
                full_name=full_name,
                username=username,
                user_id=user_id,
                money=0,
                linking=linking,
                parent_id=7,
                count=0,
                is_try='no'
            )

    except Exception as error:
        logging.info(error)

    try:
        selection = await db.select_all_sponsors()

        user_select = await db.select_one_user(user_id=user_id)
        is_try = user_select[0][11]

        if selection:
            pass

        else:
            start_text = "<b>Assalomu aleykum hurmatli mijoz! Siz bu bot orqali kriptovalyutalarga investitsiya " \
                         "kiritib olishingiz mumkin</b>"

            if int(ADMINS[0]) == int(user_id):
                if is_try == 'no':
                    if parent_id:
                        if int(parent_id) != int(user_id):
                            await db.update_user_count(user_id=int(parent_id))
                            await bot.send_message(chat_id=parent_id, text="Sizning hisobingizga $5 qo'shildi✅")
                            await db.update_user_money(user_id=int(parent_id))
                            await db.update_user_is_try(is_try='yes', user_id=user_id)
                            await message.answer(text=start_text, reply_markup=start_admin)
                        else:
                            await message.answer(text=start_text, reply_markup=start_admin)
                    else:
                        await message.answer(text=start_text, reply_markup=start_admin)
                else:
                    await message.answer(text=start_text, reply_markup=start_admin)

            else:
                if is_try == 'no':
                    if parent_id:
                        if int(parent_id) != int(user_id):
                            await db.update_user_count(user_id=int(parent_id))
                            await bot.send_message(chat_id=parent_id, text="Sizning hisobingizga $5 qo'shildi✅")
                            await db.update_user_money(user_id=int(parent_id))
                            await db.update_user_is_try(is_try='yes', user_id=user_id)
                            await message.answer(text=start_text, reply_markup=start)
                        else:
                            await message.answer(text=start_text, reply_markup=start)
                    else:
                        await message.answer(text=start_text, reply_markup=start)
                else:
                    await message.answer(text=start_text, reply_markup=start)


    except Exception as err:
        logging.info(err)


