from loader import dp, db
from keyboards.inline.viprates import rates
from keyboards.inline.back import back

from aiogram import types
from aiogram.dispatcher import FSMContext

from states.viprates import Rate


@dp.message_handler(text="✳️ Vip tariflar", state='*')
async def vip_rates(message: types.Message, state: FSMContext):

    text = "O'zingizga kerakli bo'lgan tarifni tanlang👇"
    await message.answer(text=text, reply_markup=rates)
    await Rate.rates.set()


@dp.callback_query_handler(text="premiumbtc", state=Rate.rates)
async def premium_func_btc(call: types.CallbackQuery, state: FSMContext):
    text = "Premium BTC 👇\n\n Premium BTC <code>5%</code>\n🧾Shartnoma <code>30</code> kun\n" \
           "Minimal summa: <code>1.000.000</code> sum"
    await call.message.edit_text(text=text, reply_markup=back)

