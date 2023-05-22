from loader import dp, db
from keyboards.inline.viprates import rates
from keyboards.inline.back import back_btc, back_eth, back_ltc

from aiogram import types
from aiogram.dispatcher import FSMContext

from states.viprates import Rate

from language import i18n

_ = i18n.gettext


@dp.message_handler(text=[_("✳️ Vip tariflar"), "✳️ VIP тарифы"], state='*')
async def vip_rates(message: types.Message, state: FSMContext):
    text = _("<b>O'zingizga kerakli bo'lgan tarifni tanlang👇</b>")
    await message.answer(text=text, reply_markup=rates)
    await Rate.rates.set()


@dp.callback_query_handler(text="premiumbtc", state=Rate.rates)
async def premium_func_btc(call: types.CallbackQuery, state: FSMContext):
    text = _("Premium BTC 👇\n\nPremium BTC <code>3.4%</code>\n🧾Shartnoma <code>30</code> kun\n"
             "Minimal summa: <code>1.000.000</code> sum")
    await call.message.edit_text(text=text, reply_markup=back_btc)

    await state.update_data(
        {'current_crypto': call.data}
    )


@dp.callback_query_handler(text="standarteth", state=Rate.rates)
async def premium_func_btc(call: types.CallbackQuery, state: FSMContext):
    text = _("Standart ETH 👇\n\nStandart ETH <code>2.3%</code>\n🧾Shartnoma <code>30</code> kun\n"
             "Minimal summa: <code>500.000</code> sum")
    await call.message.edit_text(text=text, reply_markup=back_eth)

    await state.update_data(
        {'current_crypto': call.data}
    )


@dp.callback_query_handler(text="maximumltc", state=Rate.rates)
async def premium_func_btc(call: types.CallbackQuery, state: FSMContext):
    text = _("Maximum LTC 👇\n\nMaximum LTC <code>1.8%</code>\n🧾Shartnoma <code>30</code> kun\n"
             "Minimal summa: <code>300.000</code> sum")
    await call.message.edit_text(text=text, reply_markup=back_ltc)

    await state.update_data(
        {'current_crypto': call.data}
    )
