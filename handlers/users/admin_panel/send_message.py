import asyncio
import logging
from aiogram.utils.exceptions import BotBlocked

from handlers.users.detectors import detect_markups
from loader import dp, db, bot
from states.admin import Panel

from aiogram.dispatcher import FSMContext
from aiogram import types


@dp.callback_query_handler(text="send_message", state=Panel.admin_menu)
async def send_messages_to_users(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text(text="<b>Reklamani yuboring...</b>")
    await Panel.datas.set()


@dp.message_handler(state=Panel.datas, content_types=types.ContentType.PHOTO)
async def get_message_datas(message: types.Message, state: FSMContext):
    """
    For PHOTO messages
    """
    file_id = message.photo[-1].file_id

    users = await db.select_all_users()

    admin_text = f"<b>🔖Reklama <code>{len(users)}</code> ta foydalanuvchiga yuborish boshlandi</b>"
    await message.answer(text=admin_text)

    sended = 0
    unsended = 0

    if 'reply_markup' in message:
        if 'caption' in message:
            caption = message.caption
            markups = message.reply_markup.inline_keyboard

            for user in users:
                user_id = user[3]

                try:
                    await bot.send_photo(chat_id=user_id, photo=file_id, caption=caption,
                                         reply_markup=detect_markups(markups=markups))
                    await asyncio.sleep(0.5)
                    sended += 1
                except BotBlocked as botblock:
                    logging.info(botblock)
                    unsended += 1

        else:
            markups = message.reply_markup.inline_keyboard
            for user in users:
                user_id = user[3]

                try:
                    await bot.send_photo(chat_id=user_id, photo=file_id,
                                         reply_markup=detect_markups(markups=markups))
                    await asyncio.sleep(0.5)
                    sended += 1
                except BotBlocked as botblock:
                    logging.info(botblock)
                    unsended += 1

    elif 'caption' in message:
        if 'reply_markup' in message:
            caption = message.caption
            markups = message.reply_markup.inline_keyboard

            for user in users:
                user_id = user[3]

                try:
                    await bot.send_photo(chat_id=user_id, photo=file_id, caption=caption,
                                         reply_markup=detect_markups(markups=markups))
                    await asyncio.sleep(0.5)
                    sended += 1
                except BotBlocked as botblock:
                    logging.info(botblock)
                    unsended += 1

        else:
            caption = message.caption

            for user in users:
                user_id = user[3]

                try:
                    await bot.send_photo(chat_id=user_id, photo=file_id, caption=caption)
                    await asyncio.sleep(0.5)
                    sended += 1
                except BotBlocked as botblock:
                    logging.info(botblock)
                    unsended += 1

    else:
        for user in users:
            user_id = user[3]

            try:
                await bot.send_photo(chat_id=user_id, photo=file_id)
                await asyncio.sleep(0.5)
                sended += 1
            except BotBlocked as botblock:
                logging.info(botblock)
                unsended += 1

    await state.finish()

    response = f"✅ Reklama {sended} / {len(users)} ta foydalanuvchiga yuborildi\n\n" \
               f"❌ Reklama {unsended} / {len(users)} ta foydalanuvchiga yuborilmadi"
    await message.answer(text=response)


@dp.message_handler(state=Panel.datas, content_types=types.ContentType.VIDEO)
async def get_message_datas(message: types.Message, state: FSMContext):
    """
    For VIDEO messages
    """
    file_id = message.video.file_id

    users = await db.select_all_users()

    admin_text = f"<b>🔖Reklama <code>{len(users)}</code> ta foydalanuvchiga yuborish boshlandi</b>"
    await message.answer(text=admin_text)

    sended = 0
    unsended = 0

    if 'reply_markup' in message:
        if 'caption' in message:
            caption = message.caption
            markups = message.reply_markup.inline_keyboard

            for user in users:
                user_id = user[3]

                try:
                    await bot.send_video(chat_id=user_id, video=file_id, caption=caption,
                                         reply_markup=detect_markups(markups=markups))
                    await asyncio.sleep(0.5)
                    sended += 1
                except BotBlocked as botblock:
                    logging.info(botblock)
                    unsended += 1

        else:
            markups = message.reply_markup.inline_keyboard
            for user in users:
                user_id = user[3]

                try:
                    await bot.send_video(chat_id=user_id, video=file_id,
                                         reply_markup=detect_markups(markups=markups))
                    await asyncio.sleep(0.5)
                    sended += 1
                except BotBlocked as botblock:
                    logging.info(botblock)
                    unsended += 1

    elif 'caption' in message:
        if 'reply_markup' in message:
            caption = message.caption
            markups = message.reply_markup.inline_keyboard

            for user in users:
                user_id = user[3]

                try:
                    await bot.send_video(chat_id=user_id, video=file_id, caption=caption,
                                         reply_markup=detect_markups(markups=markups))
                    await asyncio.sleep(0.5)
                    sended += 1
                except BotBlocked as botblock:
                    logging.info(botblock)
                    unsended += 1

        else:
            caption = message.caption

            for user in users:
                user_id = user[3]

                try:
                    await bot.send_video(chat_id=user_id, video=file_id, caption=caption)
                    await asyncio.sleep(0.5)
                    sended += 1
                except BotBlocked as botblock:
                    logging.info(botblock)
                    unsended += 1

    else:
        for user in users:
            user_id = user[3]
            try:
                await bot.send_video(chat_id=user_id, video=file_id)
                await asyncio.sleep(0.5)
                sended += 1
            except BotBlocked as botblock:
                logging.info(botblock)
                unsended += 1

    await state.finish()

    response = f"✅ Reklama {sended} / {len(users)} ta foydalanuvchiga yuborildi\n\n" \
               f"❌ Reklama {unsended} / {len(users)} ta foydalanuvchiga yuborilmadi"
    await message.answer(text=response)



@dp.message_handler(state=Panel.datas, content_types=types.ContentType.TEXT)
async def get_message_datas(message: types.Message, state: FSMContext):
    """
    For TEXT messages
    """

    users = await db.select_all_users()

    admin_text = f"<b>🔖Reklama <code>{len(users)}</code> ta foydalanuvchiga yuborish boshlandi</b>"
    await message.answer(text=admin_text)

    sended = 0
    unsended = 0

    if 'reply_markup' in message:
        if 'text' in message:
            text = message.text
            markups = message.reply_markup.inline_keyboard

            for user in users:
                user_id = user[3]
                try:
                    await bot.send_message(chat_id=user_id, text=text,
                                         reply_markup=detect_markups(markups=markups))
                    await asyncio.sleep(0.5)
                    sended += 1
                except BotBlocked as botblock:
                    logging.info(botblock)
                    unsended += 1

        else:
            markups = message.reply_markup.inline_keyboard
            for user in users:
                user_id = user[3]
                try:
                    await bot.send_message(chat_id=user_id,
                                         reply_markup=detect_markups(markups=markups))
                    await asyncio.sleep(0.5)
                    sended += 1
                except BotBlocked as botblock:
                    logging.info(botblock)
                    unsended += 1

    elif 'text' in message:
        if 'reply_markup' in message:
            text = message.text
            markups = message.reply_markup.inline_keyboard

            for user in users:
                user_id = user[3]
                try:
                    await bot.send_message(chat_id=user_id, text=text,
                                       reply_markup=detect_markups(markups=markups))

                    await asyncio.sleep(0.5)
                    sended += 1
                except BotBlocked as botblock:
                    logging.info(botblock)
                    unsended += 1

        else:
            text = message.text

            for user in users:
                user_id = user[3]
                try:
                    await bot.send_message(chat_id=user_id, text=text)

                    await asyncio.sleep(0.5)
                    sended += 1
                except BotBlocked as botblock:
                    logging.info(botblock)
                    unsended += 1

    else:
        pass

    await state.finish()

    response = f"✅ Reklama {sended} / {len(users)} ta foydalanuvchiga yuborildi\n\n" \
               f"❌ Reklama {unsended} / {len(users)} ta foydalanuvchiga yuborilmadi"
    await message.answer(text=response)


