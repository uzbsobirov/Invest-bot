from loader import dp, db
from states.admin import Panel


from aiogram.dispatcher import FSMContext
from aiogram import types


@dp.callback_query_handler(text="subscription", state=Panel.sponsor)
async def set_sponsor(call: types.CallbackQuery, state: FSMContext):
    select_channels = await db.select_all_sponsors()

    count = 0
    text = "🗒 <b>Hozirgi ulangan kanallar ro'yhati</b>"
    if select_channels is not None:
        for sponsor in select_channels:
            chat_id = sponsor[1]
            username = sponsor[2]
            print(chat_id, username)
    else:
        await call.message.edit_text(text="Sizda hali homiy kanallar yo'q❗️")

    
