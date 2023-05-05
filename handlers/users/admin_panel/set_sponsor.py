import logging

from aiogram.utils.exceptions import BadRequest
from asyncpg import UniqueViolationError

from keyboards.default.start import start_admin
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
    if len(select_channels) != 0 and len(select_channels) >= 1:
        for sponsor in select_channels:
            chat_id = sponsor[1]
            get_datas = await bot.get_chat(chat_id=chat_id)
            text += f"{count}) <a href='{get_datas.invite_link}'>{get_datas.title}</a> | <code>{get_datas.id}</code>\n"
            count += 1
        await call.message.delete()
        await call.message.answer(text=text, reply_markup=channels_menu, disable_web_page_preview=True)
        await state.update_data(
            {'text_channels': text}
            )

    else:
        # logging.info(error)
        await call.message.edit_text(text="Sizda hali homiy kanallar yo'q❗️", reply_markup=channels_menuu)

    await Panel.sponsor.set()

@dp.callback_query_handler(text="add_channel", state=Panel.sponsor)
async def add_sponsor(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text(text="<b>Homiy kanaldan birorta xabarni forward qilib tashlang"
                                      "\n\n❗️ Bot kanalda admin bo'lishi shart</b>")
    await Panel.get_id.set()

@dp.message_handler(state=Panel.get_id, content_types=types.ContentTypes.ANY)
async def get_sponsor_channel_id(message: types.Message, state: FSMContext):
    chat_id = message.forward_from_chat.id
    print(chat_id)


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



# <-------------DELETE CHANNEL----------------->
@dp.callback_query_handler(text="channel_delete", state=Panel.sponsor)
async def delete_channel(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    text_channels = data.get('text_channels')

    select_channels = await db.select_all_sponsors()

    if select_channels != ([], ()) or len(select_channels) == 0:
        await call.message.edit_text(text=f"O'chirmoqchi bo'lgan kanal idsini kiriting👇\n{text_channels}",
                                     disable_web_page_preview=True)
        await Panel.chat_id.set()

    else:
        await call.message.edit_text(text="Sizda hali homiy kanallar yo'q❗️", reply_markup=channels_menuu)


@dp.message_handler(state=Panel.chat_id)
async def get_deleted_channel_id(message: types.Message, state: FSMContext):
    try:
        chat_id = int(message.text)
        await db.delete_channel(chat_id=chat_id)
        await message.answer(text="Kanal homiylar ro'yhatidan o'chirildi✅", reply_markup=start_admin)
        await state.finish()
    except ValueError as valerr:
        logging.info(valerr)
        await message.answer(text="Faqat homiy id sini kiriting!!!")
        await Panel.chat_id.set()
    
