import asyncio
import logging

import asyncpg

from data.config import ADMINS
from keyboards.default.start import start, start_admin
from loader import dp, db, bot
from states.admin import Panel

from aiogram.dispatcher import FSMContext
from aiogram import types

from language import i18n

_ = i18n.gettext


@dp.callback_query_handler(text="send_message", user_id=ADMINS, state=Panel.admin_menu)
async def repost(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text(_("<b>Reklamani yuboring...</b>"))
    await Panel.datas.set()


@dp.message_handler(content_types=types.ContentTypes.ANY, user_id=ADMINS, state=Panel.datas)
async def send_post_all_groups(message: types.Message, state: FSMContext):
    users = await db.select_all_users()

    admin_text = _("<b>🔖Reklama <code>{}</code> ta foydalanuvchiga yuborish boshlandi</b>".format(len(users)))
    await message.answer(text=admin_text)

    sended = 0
    unsended = 0

    try:
        for user in users:
            user_id = user[3]
            try:
                await message.send_copy(chat_id=user_id)
                sended += 1
                await asyncio.sleep(0.05)
            except Exception as error:
                logging.info(error)
                unsended += 1
                continue

    except asyncpg.exceptions as error:
        logging.info(error)
        await message.answer(_("Uzur xatolik yuz berdi, keyinroq urinib ko'ring!"))

    except Exception as error:
        logging.info(error)
        pass

    finally:
        response = _("✅ Reklama {} / {} ta foydalanuvchiga yuborildi\n\n❌ Reklama {} / {} ta foydalanuvchiga yuborilmadi".format(sended, len(users), unsended, len(users)))
        await message.answer(text=response, reply_markup=start_admin)
        await state.finish()
