import logging

from keyboards.inline.balance import withdraw, payment
from loader import dp, db, bot
from states.balance import Balance
from .detectors import input_sum, crypto, percent

from aiogram.dispatcher import FSMContext
from aiogram import types

@dp.message_handler(text="💰 Balans", state='*')
async def uer_balance(message: types.Message, state: FSMContext):
    user_id = message.from_user.id

    select_user = await db.select_one_user(user_id=user_id)
    input_money = select_user[0][6]
    cripto = select_user[0][4]
    percentt = select_user[0][7]

    text = f"💰 Kiritgan summa: {input_sum(item=input_money)}\n" \
           f"🔹 Kriptovalyuta: {crypto(item=cripto)}\n⏳ Kunlik foiz: {percent(item=percentt)}"
    await message.answer(text=text, reply_markup=withdraw)
    await Balance.withdraw.set()

@dp.callback_query_handler(state=Balance.withdraw)
async def withdrwa_money(call: types.CallbackQuery, state: FSMContext):
    text = "<b>Karta raqami va karta kimni nomida ekanligini ko'rsating👇\n\n" \
           "<code>8600777766668888/Falonchi Falonchiyev</code></b>"
    await call.message.edit_text(text=text)
    await Balance.data.set()

@dp.message_handler(state=Balance.data)
async def get_card_data(message: types.Message, state: FSMContext):
    msg = message.text
    full_name = message.from_user.full_name
    user_mention = message.from_user.get_mention(name=full_name)
    user_id = message.from_user.id

    try:
        splited = msg.split('/')
        card = splited[0]
        owner = splited[1]
        if (len(card) == 16 and card.startswith('8600') or (len(card) == 16 and card.startswith('9860'))):
            await message.answer(text="Admin tez orada to'lov qiladi")
            await bot.send_message(chat_id=-1001749997672,
                                   text=f"{user_mention} pul yechib olmoqchi\n\n"
                                        f"👤 <code>{owner}</code>\n💳 <code>{card}</code>\n💰 None"
                                   , reply_markup=payment)

            await state.finish()
        else:
            await message.answer(text="Yaroqsiz karta boshqattan kiriting\n\n"
                                      "<code>8600777766668888/Falonchi Falonchiyev</code>")
            await Balance.data.set()
    except Exception as error:
        logging.info(error)
        await message.answer(text="Yaroqsiz karta boshqattan kiriting\n\n"
                                  "<code>8600777766668888/Falonchi Falonchiyev</code>")
        await Balance.data.set()



