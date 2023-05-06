from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from loader import dp, db, bot
from states.admin import Panel
from utils.misc.subs import check
from data.config import ADMINS
from keyboards.default.start import start, start_admin


@dp.callback_query_handler(text="check_subs", state='*')
async def check_func(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    parent_id = data.get('parent_id')
    print(parent_id)
    print('/check')

    main_text = "<b>Assalomu aleykum hurmatli mijoz! Siz bu bot orqali kriptovalyutalarga " \
                "investitsiya kiritib olishingiz mumkin</b>"

    notif_user = "<b>Sizning hisobingizga 50.000 so'n qo'shildi</b>"

    user_id = call.from_user.id
    full_name = call.from_user.id

    await call.answer("Obuna tekshirilmoqda...")
    final_status = True

    result = InlineKeyboardMarkup(row_width=1)

    lst_channels = await db.select_all_sponsors()
    # rows = await db.select_row_panel()
    # if len(lst_channels) >= 1:
    for channel in lst_channels:
        status = await check(user_id=call.from_user.id, channel=channel[1])
        channel = await bot.get_chat(channel[1])
        invite_link = await channel.export_invite_link()
        if status is not True:
            final_status *= False
            result.insert(InlineKeyboardButton(text=f"❌ {channel.title}", url=invite_link))
    result.add(InlineKeyboardButton(text="✅ Obunani tekshirish", callback_data='check_subs'))

    if final_status:
        await call.message.delete()

        user_select = await db.select_one_user(user_id=user_id)
        is_try = user_select[0][11]

        if user_id != int(ADMINS[0]):
            if parent_id:
                if is_try != 'yes':
                    await db.update_user_count(user_id=int(parent_id))
                    await db.update_user_money(money=50000, user_id=int(parent_id))
                    await db.update_user_is_try(is_try='yes', user_id=user_id)
                    print('/check yes 2')
                    await bot.send_message(chat_id=parent_id, text=notif_user)
                    await call.message.answer(text=main_text, reply_markup=start)

                else:
                    await call.message.answer(text=main_text, reply_markup=start_admin)

            else:
                await call.message.answer(text=main_text, reply_markup=start_admin)

        else:
            await call.message.answer(text=main_text, reply_markup=start_admin)

        if user_id != int(ADMINS[0]):
            if parent_id:

                if is_try != 'yes':

                    await db.update_user_count(user_id=int(parent_id))
                    await db.update_user_money(money=50000, user_id=int(parent_id))
                    await db.update_user_is_try(is_try='yes', user_id=user_id)
                    print('/check yes 2')
                    await bot.send_message(chat_id=parent_id, text=notif_user)

                    await call.message.answer(text=main_text, reply_markup=start)


                else:

                    await call.message.answer(text=main_text, reply_markup=start_admin)


            else:

                await call.message.answer(text=main_text, reply_markup=start_admin)


        else:

            await call.message.answer(text=main_text, reply_markup=start_admin)

        await state.finish()
    else:
        await call.message.delete()
        await call.message.answer(text="<b>❌Siz ba'zi kanallardan chiqib ketgansiz, agar kanallarga "
                                       "ulanmasangiz botni ishlata olmaysiz</b>", reply_markup=result,
                                  disable_web_page_preview=True)


