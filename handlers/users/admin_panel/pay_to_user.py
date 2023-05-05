import asyncio
import logging
import schedule
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from handlers.users import everyday_pay

from data.config import ADMINS
from handlers.users.detectors import detect_crypto, detect_percent, detect_crypto_money
from handlers.users.everyday_pay import pay_time_schedule
from loader import dp, bot, db
from states.paying import Pay
from states.buycrypto import EveryDay
from keyboards.inline.admin import cryptos

from aiogram import types
from aiogram.dispatcher import FSMContext

scheduler = AsyncIOScheduler()

@dp.callback_query_handler(text="pay_to_user", state='*')
async def payload_user(call: types.CallbackQuery, state: FSMContext):

    text = "<b>Foydalanuvchi idsini kiriting👇</b>"
    await call.message.edit_text(text=text)
    await Pay.id.set()

@dp.message_handler(state=Pay.id)
async def get_user_id(message: types.Message, state: FSMContext):

    try:
        id = int(message.text)

        select_user = await db.select_one_user(user_id=id)
        customer_crypto = select_user[0][4]

        if customer_crypto:
            await message.answer(text=f"Kechirasiz bu foydalanuvchi "
                                      f"<code>{detect_crypto(crypto=customer_crypto)}</code> ni sotib olgan ekan")

        else:
            await state.update_data(
                {'customer_id': id}
            )
            await message.answer(text="Yaxshi endi foydalanuvchi qaysi kriptovalyuta olganini tanlang👇",
                                 reply_markup=cryptos)
            await Pay.crypto.set()
    except Exception as error:
        logging.info(error)
        await message.answer(text="Iltimos faqat raqamlardan foydalaning\n\nNamuna: <code>1393587687</code>")
        await Pay.id.set()

@dp.callback_query_handler(state=Pay.crypto)
async def get_crypto(call: types.CallbackQuery, state: FSMContext):
    data = call.data
    await state.update_data(
        {'customer_crypto': data}
    )

    await call.message.edit_text(text="Yaxshi endi foydalanuvchi balansini "
                                      "nechi so'm bilan to'ldirmoqchi ekanliginzini yozing"
                                      "\n\nNamuna: <code>50000</code>")
    await Pay.money.set()

@dp.message_handler(state=Pay.money)
async def get_money(message: types.Message, state: FSMContext):
    data = await state.get_data()
    customer_id = data.get('customer_id')
    customer_crypto = data.get('customer_crypto')

    # try:
    money = int(message.text)

    await bot.send_message(chat_id=message.chat.id, text=f"Foydalanuvchi balansi {money} so'm bilan to'ldirildi✅")
    await bot.send_message(chat_id=customer_id, text=f"Hisobingiz {money} so'm bilan to'ldirildi, "
                                                     f"iltimos hisobingizni tekshiring")

    before_select_user = await db.select_one_user(user_id=customer_id)
    before_money = before_select_user[0][5]
    set_current_money = money + before_money
    await db.update_user_money_pay(money=set_current_money,
                                                crypto=customer_crypto, date=30, user_id=customer_id)


    scheduler.add_job(everyday_pay.pay_time_schedule, 'interval', minutes=1440, kwargs={'user_id': int(customer_id)})
    await state.finish()

    # await pay_time_schedule()

    # get_datas = await db.select_one_user(user_id=customer_id)
    #
    # current_money = get_datas[0][5]
    # crypto = get_datas[0][4]
    # date = get_datas[0][12]
    #
    # for _ in range(1, 31):
    #     if date > 0:
    #         if current_money > detect_crypto_money(crypto=crypto):
    #             percent = (current_money * detect_percent(crypto=crypto)) / 100
    #
    #             changed_money = current_money + percent
    #
    #             await db.update_user_new_money(money=changed_money, user_id=customer_id)
    #
    #             await db.update_user_date(user_id=customer_id)
    #             await asyncio.sleep(3)


    # except Exception as error:
    #     logging.info(error)
    #     await message.answer(text="Iltimos faqat raqamlardan foydalaning\n\nNamuna: <code>1393587687</code>")
    #     await Pay.id.set()

# @dp.message_handler()

