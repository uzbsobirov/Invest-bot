from datetime import datetime, date, timedelta

from loader import dp, db, bot
from keyboards.inline.back import back

from aiogram import types
from aiogram.dispatcher import FSMContext

from states.admin import Panel

from language import i18n

_ = i18n.gettext


@dp.callback_query_handler(text="statistic", state=Panel.admin_menu)
async def admin_menu_statics(call: types.CallbackQuery, state: FSMContext):
    get_me = await bot.get_me()
    bot_username = get_me.username

    todays_date = date.today()  # Todays date
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    all_users = await db.select_all_users()

    text = _("<b>📅 Bugungi sana: {}\n🕰 Hozirgi vaqt: {}\n\n📊 Bot obunachilari soni: {}\n\n⚡️ @{}</b>".format(todays_date, current_time, len(all_users), bot_username))

    await call.message.edit_text(text=text, reply_markup=back)
    await Panel.statics.set()