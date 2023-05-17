import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.utils.deep_linking import get_start_link

from data.config import ADMINS
from keyboards.default.start import start, start_admin
from keyboards.inline.lang import langs
from loader import dp, db, bot

from language import i18n

_ = i18n.gettext


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message, state: FSMContext):
    full_name = message.from_user.full_name
    username = message.from_user.username
    user_id = message.from_user.id
    user_mention = message.from_user.get_mention(name=full_name, as_html=True)
    linking = await get_start_link(user_id)
    parent_id = message.get_args()

    main_text = _("<b>Assalomu aleykum hurmatli mijoz! Siz bu bot orqali "
                  "kriptovalyutalarga investitsiya kiritib olishingiz mumkin</b>")

    notif_user = _("<b>Sizning hisobingizga 50.000 so'n qo'shildi</b>")

    await state.update_data(
        {'parent_id': parent_id}
    )

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

    user_select = await db.select_user_lang(user_id=user_id)
    user_lang = user_select[0][4]

    if user_lang != 'null':
        if parent_id:
            if user_id != ADMINS[0]:
                await db.update_user_money(money=50000, user_id=int(parent_id))
                await db.update_user_count(user_id=int(parent_id))
                await bot.send_message(chat_id=int(parent_id), text='На ваш счет добавлено $5')
                await bot.send_message(chat_id=message.chat.id, text=main_text, reply_markup=start)
            else:
                await bot.send_message(chat_id=message.chat.id, text=main_text, reply_markup=start_admin)

        else:
            if user_id != ADMINS[0]:
                await bot.send_message(chat_id=message.chat.id, text=main_text, reply_markup=start)
            else:
                await bot.send_message(chat_id=message.chat.id, text=main_text, reply_markup=start_admin)
    else:
        text = "🇺🇿 Tilni tanlang:\n🇷🇺 Выберите язык:"
        await message.answer(text=text, reply_markup=langs)
