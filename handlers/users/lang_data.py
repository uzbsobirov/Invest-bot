from data.config import ADMINS
from keyboards.default.start import start, start_admin
from loader import dp, db, bot

from aiogram import types
from aiogram.dispatcher import FSMContext

from language import i18n

_ = i18n.gettext


@dp.callback_query_handler(text="uz", state='*')
async def uz_lang(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()

    data = await state.get_data()
    parent_id = data.get('parent_id')

    user_id = call.from_user.id

    await call.answer(text="🇺🇿 O'zbek tili tanlandi", cache_time=3)

    await db.update_user_language(lang='uz', user_id=user_id)

    main_text = _("<b>Assalomu aleykum hurmatli mijoz! Siz bu bot orqali "
                  "kriptovalyutalarga investitsiya kiritib olishingiz mumkin</b>")

    if parent_id:
        if user_id != ADMINS[0]:
            await db.update_user_money(money=50000, user_id=int(parent_id))
            await db.update_user_count(user_id=int(parent_id))
            await bot.send_message(chat_id=int(parent_id), text='Hisobingizga $5 qo\'shildi')
            await bot.send_message(chat_id=call.message.chat.id, text=main_text, reply_markup=start)
        else:
            await bot.send_message(chat_id=call.message.chat.id, text=main_text, reply_markup=start_admin)

    else:
        if user_id != ADMINS[0]:
            await bot.send_message(chat_id=call.message.chat.id, text=main_text, reply_markup=start)
        else:
            await bot.send_message(chat_id=call.message.chat.id, text=main_text, reply_markup=start_admin)


@dp.callback_query_handler(text="ru", state='*')
async def uz_lang(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()

    data = await state.get_data()
    parent_id = data.get('parent_id')
    print(parent_id)
    user_id = call.from_user.id

    await call.answer(text="🇷🇺 Выбран русский язык", cache_time=3)

    await db.update_user_language(lang='ru', user_id=user_id)

    main_text = _("<b>Assalomu aleykum hurmatli mijoz! Siz bu bot orqali "
                  "kriptovalyutalarga investitsiya kiritib olishingiz mumkin</b>")

    if parent_id:
        if user_id != ADMINS[0]:
            await db.update_user_money(money=50000, user_id=int(parent_id))
            await db.update_user_count(user_id=int(parent_id))
            await bot.send_message(chat_id=int(parent_id), text='На ваш счет добавлено $5')
            await bot.send_message(chat_id=call.message.chat.id, text=main_text, reply_markup=start)
        else:
            await bot.send_message(chat_id=call.message.chat.id, text=main_text, reply_markup=start_admin)

    else:
        if user_id != ADMINS[0]:
            await bot.send_message(chat_id=call.message.chat.id, text=main_text, reply_markup=start)
        else:
            await bot.send_message(chat_id=call.message.chat.id, text=main_text, reply_markup=start_admin)
