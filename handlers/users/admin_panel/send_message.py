import logging

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
    file_id = message.photo[-1].file_id

    users = await db.select_all_users()

    if 'reply_markup' in message:
        if 'caption' in message:
            caption = message.caption
            markups = message.reply_markup.inline_keyboard

            for user in users:
                user_id = user[3]
                await bot.send_photo(chat_id=user_id, photo=file_id, caption=caption,
                                     reply_markup=detect_markups(markups=markups))

        else:
            print('markup')

    elif 'caption' in message:
        if 'reply_markup' in message:
            print('ikkisam bo')
        else:
            print('caption')

    else:
        print('ikkisam yoq')

    # try:
    #     caption = message.caption
    #     markups = message.reply_markup.inline_keyboard
    #     if markups and caption:
    #         for item in markups:
    #             print(f'{item[0].text} -- {item[0].url} -- {caption}')
    #     elif markups:
    #         print('caption yoq')
    #     elif caption:
    #         print('markup yoq')
    #     else:
    #         print('ikkisam yoq')
    #
    # except AttributeError as error:
    #     logging.info(error)
    #     print(file_id)