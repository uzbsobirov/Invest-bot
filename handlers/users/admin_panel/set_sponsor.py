import logging

from aiogram.utils.exceptions import BadRequest
from asyncpg import UniqueViolationError

from keyboards.inline.back import back_sponsor
from loader import dp, db, bot
from states.admin import Panel
from keyboards.inline.admin import channels_menu, channels_menuu

from aiogram.dispatcher import FSMContext
from aiogram import types

from utils.misc.is_admin import check_is_admin


@dp.callback_query_handler(text="subscription", state=Panel.admin_menu)
async def set_sponsor(call: types.CallbackQuery, state: FSMContext):
    select_channels = await db.select_all_sponsors()

    count = 1
    text = "🗒 <b>Hozirgi ulangan kanallar ro'yhati\n\n</b>"
    try:
        for sponsor in select_channels:
            chat_id = sponsor[1]
            get_datas = await bot.get_chat(chat_id=chat_id)
            text += f"{count}) <a href='{get_datas.invite_link}'>{get_datas.title}</a> | <code>{get_datas.id}</code>\n"
            count += 1
        await call.message.delete()
        await call.message.answer(text=text, reply_markup=channels_menu, disable_web_page_preview=True)
    except Exception as error:
        logging.info(error)
        await call.message.edit_text(text="Sizda hali homiy kanallar yo'q❗️", reply_markup=channels_menuu)

    await Panel.sponsor.set()

@dp.callback_query_handler(text="add_channel", state=Panel.sponsor)
async def add_sponsor(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text(text="<b>Homiy kanaldan birorta xabarni forward qilib tashlang"
                                      "\n\n❗️ Bot kanalda admin bo'lishi shart</b>")
    await Panel.get_id.set()

@dp.message_handler(state=Panel.get_id)
async def get_sponsor_channel_id(message: types.Message, state: FSMContext):
    chat_id = message.forward_from_chat.id
    title = message.forward_from_chat.title
    username = message.forward_from_chat.username


    get_me = await bot.get_me()
    bot_username = get_me.username

    try:
        checking = await check_is_admin(channel=chat_id)

        for item in checking:
            if item.status == 'administrator' and item.user.username == bot_username:
                await message.answer(text="Kanal Majburiy obuna bo'limiga qo'shildi✅", reply_markup=back_sponsor)
                await db.add_sponsor(chat_id=chat_id)
                break
            else:
                await message.answer(text="Bot kanalda admin emas! Botni admin qilib qaytadan urinib ko'ring")
                await Panel.get_id.set()
    except BadRequest as error:
        logging.info(error)
        await message.answer(text="Bot kanalda admin emas! Botni admin qilib qaytadan urinib ko'ring")
        await Panel.get_id.set()

    except UniqueViolationError as err:
        logging.info(err)
        await message.answer(text="Bu kanal aval qo'shilgan ekan")
        await Panel.get_id.set()

    
