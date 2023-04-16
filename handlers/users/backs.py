from keyboards.inline.cards import cards
from loader import dp
from states.buycrypto import Buy
from states.viprates import Rate
from keyboards.default.start import start
from keyboards.inline.viprates import rates

from aiogram import types
from aiogram.dispatcher import FSMContext

@dp.callback_query_handler(text="back_to_main", state='*')
async def back_to_main(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()

    start_text = "<b>Assalomu aleykum hurmatli mijoz! Siz bu bot orqali kriptovalyutalarga investitsiya " \
                 "kiritib olishingiz mumkin</b>"
    await call.message.answer(text=start_text, reply_markup=start)
    await state.finish()

@dp.callback_query_handler(text="back", state=Rate.rates)
async def back_to_rates(call: types.CallbackQuery, state: FSMContext):

    text = "O'zingizga kerakli bo'lgan tarifni tanlang👇"
    await call.message.edit_text(text=text, reply_markup=rates)
    await Rate.rates.set()

@dp.callback_query_handler(text="back_to_rates", state=Buy.crypto)
async def back_to_rates(call: types.CallbackQuery, state: FSMContext):

    text = "O'zingizga kerakli bo'lgan tarifni tanlang👇"
    await call.message.edit_text(text=text, reply_markup=rates)
    await Rate.rates.set()

@dp.callback_query_handler(text="back_to_cards", state=Buy.crypto)
async def back_to_rates(call: types.CallbackQuery, state: FSMContext):

    text = "<b>📋Quyidagi to'lov turlaridan birini tanlang:</b>"
    await call.message.edit_text(text=text, reply_markup=cards)
    await Buy.crypto.set()