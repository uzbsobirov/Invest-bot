import logging

from data.config import ADMINS
from keyboards.default.start import start
from keyboards.inline.balance import withdraw, payment
from loader import dp, db, bot
from states.balance import Balance
from handlers.detectors import sum_input, crypto, percent

from aiogram.dispatcher import FSMContext
from aiogram import types

from language import i18n
from states.paying import PayTime

_ = i18n.gettext


@dp.message_handler(text=[_("💰 Balans"), "💰 Баланс"], state='*')
async def uer_balance(message: types.Message, state: FSMContext):
    user_id = message.from_user.id

    select_user = await db.select_one_user(user_id=user_id)
    input_money = select_user[0][6]
    cripto = select_user[0][4]
    percentt = select_user[0][7]
    current_balance = select_user[0][5]

    text = _(
        "💰 Kiritgan summa: {}\n🔹 Kriptovalyuta: {}\n⏳ Kunlik foiz: {}\n💸 Hozirgi balans: {} so'm\n\n💰Eng kam yechib olish 10 $\n💰Eng ko'p yechib olish 10000$\n🏛️Hisobingizga 48 soat davomida òtkaziladi✅".format(
            sum_input(item=input_money), crypto(item=cripto), percent(item=percentt), current_balance))
    await message.answer(text=text, reply_markup=withdraw)
    await Balance.withdraw.set()


@dp.callback_query_handler(state=Balance.withdraw)
async def withdrwa_money(call: types.CallbackQuery, state: FSMContext):
    text = _("<b>Karta raqami va karta kimni nomida ekanligini ko'rsating👇\n\n"
             "<code>8600777766668888/Falonchi Falonchiyev</code></b>")
    await call.message.edit_text(text=text)
    await Balance.data.set()


@dp.message_handler(state=Balance.data)
async def get_card_data(message: types.Message, state: FSMContext):
    msg = message.text
    full_name = message.from_user.full_name
    user_mention = message.from_user.get_mention(name=full_name)
    user_id = message.from_user.id

    await state.update_data(
        {'user_id': user_id}
    )

    select_user = await db.select_one_user(user_id=user_id)

    try:
        splited = msg.split('/')
        card = splited[0]
        owner = splited[1]
        balance = select_user[0][5]
        if balance >= 100000:
            if len(card) == 16 and card.startswith('8600') or (len(card) == 16 and card.startswith('9860')):
                await message.answer(text=_("Admin tez orada to'lov qiladi"))
                await bot.send_message(chat_id=ADMINS[0],
                                       text=f"{user_mention} [<code>{user_id}</code>] pul yechib olmoqchi\n\n👤 <code>{owner}</code>\n"
                                            f"💳 <code>{card}</code>\n💰 {balance} so'm"
                                       , reply_markup=payment)

                await state.finish()
            else:
                await message.answer(text=_("Yaroqsiz karta boshqattan kiriting\n\n"
                                            "<code>8600777766668888/Falonchi Falonchiyev</code>"))
                await Balance.data.set()
        else:
            await message.answer(text=_("<b>Botdan faqat eng kam miqdorda 100.000 so'm chiqarib olishingiz mumkin</b>"),
                                 reply_markup=start)
            await state.finish()
    except Exception as error:
        logging.info(error)
        await message.answer(text=_("Yaroqsiz karta boshqattan kiriting\n\n"
                                    "<code>8600777766668888/Falonchi Falonchiyev</code>"))
        await Balance.data.set()


@dp.callback_query_handler(text="successpay", state='*')
async def withdraw_user_balance(call: types.CallbackQuery, state: FSMContext):
    text = "Pul kiritmoqchi bo'lgan foydalanuvchining idsini kiriting"
    await call.message.answer(text=text)
    await PayTime.id.set()


@dp.message_handler(state=PayTime.id)
async def get_user_id(message: types.Message, state: FSMContext):
    user_id = message.text

    if user_id.isalnum():
        await state.update_data(
            {'user_id': user_id}
        )
        text = "Yaxshi endi nech pul kiritmoqchi ekanligingizni yozing\n\nNamnuna: 10000"
        await message.answer(text=text)
        await PayTime.money.set()

    else:
        text = "Faqat raqamlardan foydalaning"
        await message.edit_text(text=text)
        await PayTime.id.set()


@dp.message_handler(state=PayTime.money)
async def get_user_money(message: types.Message, state: FSMContext):
    data = await state.get_data()
    user_id = data.get('user_id')

    money = message.text

    if money.isalnum():
        user_selection = await db.select_one_user(user_id=int(user_id))
        balance = user_selection[0][5]

        if balance >= int(money):
            await db.update_user_new_money(money=0, user_id=int(user_id))
            await db.update_user_crypto(crypto=None, user_id=int(user_id))
            await bot.send_message(chat_id=message.chat.id, text="To'lov qilindi")
            await bot.send_message(chat_id=int(user_id), text="To'lov kartangizga o'tkazildi")
    else:
        text = "Faqat raqamlardan foydalaning"
        await message.edit_text(text=text)
        await PayTime.id.set()
