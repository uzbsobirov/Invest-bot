import asyncio
from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import ADMINS
from keyboards.inline.admin import admin
from loader import dp, db, bot
from states.admin import Panel

from language import i18n

_ = i18n.gettext


@dp.message_handler(text="/reklama", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    users = await db.select_all_users()
    for user in users:
        user_id = user[0]
        await bot.send_message(chat_id=user_id, text="@BekoDev kanaliga obuna bo'ling!")
        await asyncio.sleep(0.05)


@dp.message_handler(text=[_("💻 Admin panel"), "💻 Панель администратора"], state='*', user_id=ADMINS[0])
async def admin_panel(message: types.Message, state: FSMContext):
    await message.answer(text=_("<b>Admin panelga xush kelibsiz</b>"), reply_markup=admin)
    await Panel.admin_menu.set()
